from fastapi import APIRouter
from services.vector import create_embeddings

router = APIRouter()

@router.post("/create-embeddings")
async def create_embedding():
    try:
        create_embeddings()
        return {"message": "Embeddings created successfully"}
    except Exception as e:
        return {"error": str(e)}
