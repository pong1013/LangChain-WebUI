from fastapi import APIRouter
from controllers import chat, document, embedding

router = APIRouter()

# 包含各個路由模組
router.include_router(chat.router, prefix="/chat", tags=["Chat"])
router.include_router(document.router, prefix="/documents", tags=["Documents"])
router.include_router(embedding.router, prefix="/embedding", tags=["Embedding"])
