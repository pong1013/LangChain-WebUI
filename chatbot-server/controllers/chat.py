from fastapi import APIRouter, HTTPException, status
from services.chat import get_answer
from models.user import User
from schemas.user import (
    QuestionRequest, 
    QuestionResponse, 
    UserStatusRequest, 
    UserResponse,
    ErrorResponse,
    SuccessResponse
)
from datetime import datetime, timezone
import logging

# 設置日誌
logger = logging.getLogger(__name__)

router = APIRouter()

# 記憶體中的聊天歷史 (生產環境建議使用 Redis)
chat_histories = {}

@router.post("/ask", response_model=QuestionResponse)
async def answer_question(request: QuestionRequest):
    """處理使用者問答請求"""
    try:
        logger.info(f"Received question from {request.user_email}: {request.question}")

        # 取得或創建使用者記錄
        user = await User.get_or_create(request.user_email)
        
        # 檢查管理員權限
        if user.is_admin:
            remaining_questions = "Unlimited"
        else:
            # 檢查並增加問題計數
            if not await user.increment_question_count():
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You have reached your daily question limit. Please try again tomorrow.",
                )
            
            remaining_questions = user.get_remaining_questions()

        # 取得使用者聊天歷史
        if request.user_email not in chat_histories:
            chat_histories[request.user_email] = []
        user_chat_history = chat_histories[request.user_email]
        
        # 取得答案
        answer, updated_chat_history = get_answer(request.question, user_chat_history)
        chat_histories[request.user_email].extend(updated_chat_history)

        logger.info(f"Generated answer for {request.user_email}")

        # 返回回應
        return QuestionResponse(
            question=request.question,
            answer=answer,
            remaining_questions=remaining_questions,
            is_admin=user.is_admin
        )
        
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Internal server error: {str(e)}"
        )

@router.get("/clean-chat-history", response_model=SuccessResponse)
async def clean_chat_history():
    """清理所有聊天歷史"""
    try:
        chat_histories.clear()
        logger.info("Chat history cleaned successfully")
        return SuccessResponse(message="Chat history cleaned successfully")
    except Exception as e:
        logger.error(f"Error cleaning chat history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error cleaning chat history"
        )

@router.get("/user-status", response_model=UserResponse)
async def get_user_status(user_email: str):
    """取得使用者狀態"""
    try:
        # 取得使用者記錄
        user = await User.get_or_create(user_email)
        
        # 計算剩餘問題數
        if user.is_admin:
            remaining_questions = "Unlimited"
        else:
            remaining_questions = user.get_remaining_questions()

        logger.info(f"Retrieved status for user: {user_email}")

        return UserResponse(
            email=user.email,
            is_admin=user.is_admin,
            remaining_questions=remaining_questions,
            today_used=user.get_today_question_count(),
            created_at=user.created_at.isoformat(),
            updated_at=user.updated_at.isoformat()
        )
        
    except Exception as e:
        logger.error(f"Error fetching user status: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error fetching user status"
        )

@router.post("/reset-daily-count", response_model=SuccessResponse)
async def reset_daily_count(request: UserStatusRequest):
    """重置使用者每日計數 (僅管理員可用)"""
    try:
        user = await User.get_or_create(request.user_email)
        
        if not user.is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only administrators can reset daily counts"
            )
        
        success = await user.reset_daily_count()
        if success:
            logger.info(f"Reset daily count for user: {request.user_email}")
            return SuccessResponse(message="Daily count reset successfully")
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to reset daily count"
            )
            
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error resetting daily count: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error resetting daily count"
        )
