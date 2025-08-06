from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import routers
from config.database import init_db, close_db
import sys
import os
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 資料庫生命週期管理
async def lifespan(app: FastAPI):
    print("🚀 Starting up...")
    await init_db()  # 初始化 MongoDB
    yield
    print("🔄 Shutting down...")
    await close_db()  # 關閉資料庫連接

app = FastAPI(
    title="LangChain ChatBot API",
    description="基於 LangChain 的智能聊天機器人 API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 引入路由
app.include_router(routers.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
