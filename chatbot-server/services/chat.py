from langchain.chains import ConversationalRetrievalChain
from services.vector import load_vector_store
from config.openai import chat_model
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 載入向量資料庫
docsearch = load_vector_store()

# 初始化對話檢索鏈
qa_chain = ConversationalRetrievalChain.from_llm(
    chat_model, 
    retriever=docsearch.as_retriever()
)

def get_answer(question: str, chat_history: list) -> tuple[str, list]:
    """
    取得問題的答案
    
    Args:
        question: 使用者問題
        chat_history: 聊天歷史記錄
        
    Returns:
        tuple: (答案, 更新的聊天歷史)
    """
    try:
        logger.info(f"Processing question: {question}")
        
        # 使用 LangChain 生成答案
        result = qa_chain({
            "question": question, 
            "chat_history": chat_history
        })
        
        answer = result["answer"]
        logger.info(f"Generated answer successfully")
        
        # 返回答案和更新的聊天歷史
        return answer, [(question, answer)]
        
    except Exception as e:
        logger.error(f"Error generating answer: {str(e)}")
        raise e
