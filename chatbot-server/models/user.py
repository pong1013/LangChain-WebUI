from beanie import Document
from typing import Dict, Optional, ClassVar
from datetime import datetime, timezone
from pymongo.errors import DuplicateKeyError
from pydantic import EmailStr, Field, validator
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
ADMIN_USER = os.getenv("ADMIN_USER")

class User(Document):
    """使用者模型 - 管理使用者權限和問答計數"""
    
    email: EmailStr = Field(..., description="使用者郵箱地址")
    questions_by_date: Dict[str, int] = Field(default_factory=dict, description="每日問題計數")
    is_admin: bool = Field(default=False, description="是否為管理員")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # 每日問題限制
    DAILY_QUESTION_LIMIT: ClassVar[int] = 10

    class Settings:
        collection = "users"
        indexes = [
            "email",  # 為 email 創建索引
        ]

    @validator('email')
    def validate_email(cls, v):
        """驗證郵箱格式"""
        if not v or '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()  # 統一轉為小寫

    @classmethod
    async def get_or_create(cls, email: str) -> "User":
        """取得或創建使用者記錄"""
        try:
            # 查找現有記錄
            user = await cls.find_one({"email": email.lower()})
            
            if not user:
                # 創建新使用者
                is_admin = (email.lower() == ADMIN_USER.lower() if ADMIN_USER else False)
                user = cls(
                    email=email.lower(),
                    questions_by_date={},
                    is_admin=is_admin
                )
                await user.insert()
                print(f"Created new user: {email}")
            
            return user
            
        except DuplicateKeyError:
            # 處理重複寫入情況
            print(f"Duplicate key error for email: {email}")
            return await cls.find_one({"email": email.lower()})
        except Exception as e:
            print(f"Error creating/finding user {email}: {str(e)}")
            raise

    async def increment_question_count(self) -> bool:
        """增加今日問題計數，返回是否成功"""
        try:
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            
            # 管理員無限制
            if self.is_admin:
                self.questions_by_date[today] = self.questions_by_date.get(today, 0) + 1
                self.updated_at = datetime.now(timezone.utc)
                await self.save()
                return True
            
            # 檢查非管理員的每日限制
            current_count = self.questions_by_date.get(today, 0)
            if current_count >= self.DAILY_QUESTION_LIMIT:
                return False
            
            # 增加計數
            self.questions_by_date[today] = current_count + 1
            self.updated_at = datetime.now(timezone.utc)
            await self.save()
            
            return True
            
        except Exception as e:
            print(f"Error incrementing question count for {self.email}: {str(e)}")
            return False

    def get_remaining_questions(self) -> int:
        """取得今日剩餘問題數量"""
        if self.is_admin:
            return float("inf")  # 管理員無限制
        
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        used_count = self.questions_by_date.get(today, 0)
        return max(0, self.DAILY_QUESTION_LIMIT - used_count)

    def get_today_question_count(self) -> int:
        """取得今日已使用問題數量"""
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return self.questions_by_date.get(today, 0)

    async def reset_daily_count(self) -> bool:
        """重置今日問題計數 (僅管理員可用)"""
        if not self.is_admin:
            return False
        
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        self.questions_by_date[today] = 0
        self.updated_at = datetime.now(timezone.utc)
        await self.save()
        return True

    def to_dict(self) -> dict:
        """轉換為字典格式"""
        return {
            "email": self.email,
            "is_admin": self.is_admin,
            "remaining_questions": self.get_remaining_questions(),
            "today_used": self.get_today_question_count(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "questions_by_date": {"2024-01-15": 5},
                "is_admin": False
            }
        }
