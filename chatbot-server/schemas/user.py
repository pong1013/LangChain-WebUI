from pydantic import BaseModel, EmailStr, Field
from typing import Dict, Optional, Union
from datetime import datetime

# Request Schemas
class UserCreateRequest(BaseModel):
    """創建使用者請求"""
    email: EmailStr = Field(..., description="使用者郵箱地址")

class QuestionRequest(BaseModel):
    """問答請求"""
    question: str = Field(..., min_length=1, max_length=1000, description="問題內容")
    user_email: EmailStr = Field(..., description="使用者郵箱")

class UserStatusRequest(BaseModel):
    """使用者狀態查詢請求"""
    user_email: EmailStr = Field(..., description="使用者郵箱")

# Response Schemas
class UserResponse(BaseModel):
    """使用者資訊回應"""
    email: str
    is_admin: bool
    remaining_questions: Union[int, str]  # int 或 "Unlimited"
    today_used: int
    created_at: str
    updated_at: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "is_admin": False,
                "remaining_questions": 5,
                "today_used": 5,
                "created_at": "2024-01-15T10:30:00Z",
                "updated_at": "2024-01-15T15:45:00Z"
            }
        }

class QuestionResponse(BaseModel):
    """問答回應"""
    question: str
    answer: str
    remaining_questions: Union[int, str]
    is_admin: bool

    class Config:
        json_schema_extra = {
            "example": {
                "question": "什麼是機器學習？",
                "answer": "機器學習是人工智慧的一個分支...",
                "remaining_questions": 4,
                "is_admin": False
            }
        }

class ErrorResponse(BaseModel):
    """錯誤回應"""
    detail: str
    error_code: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "You have reached your daily question limit",
                "error_code": "DAILY_LIMIT_EXCEEDED"
            }
        }

class SuccessResponse(BaseModel):
    """成功回應"""
    message: str
    data: Optional[dict] = None

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Operation completed successfully",
                "data": {"affected_rows": 1}
            }
        } 