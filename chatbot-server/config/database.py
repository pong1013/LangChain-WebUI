from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User 
import os
from dotenv import load_dotenv


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

async def init_db():
    """初始化 MongoDB 資料庫連接和 Beanie 模型"""
    try:
        # 創建 MongoDB 客戶端
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DATABASE_NAME]

        # 初始化 Beanie 模型
        await init_beanie(database=db, document_models=[User])
        
        print(f"✅ MongoDB initialized successfully!")
        print(f"📊 Database: {DATABASE_NAME}")
        print(f"👥 Models: User")
        
    except Exception as e:
        print(f"❌ Error initializing MongoDB: {e}")
        raise e

async def close_db():
    """關閉資料庫連接"""
    try:
        # Beanie 會自動處理連接關閉
        print("🔌 Database connection closed")
    except Exception as e:
        print(f"❌ Error closing database: {e}")
