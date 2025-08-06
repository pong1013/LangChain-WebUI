# LangChain ChatBot API

基於 FastAPI 和 LangChain 的智能聊天機器人後端服務。

## 🏗️ 架構概覽

### 標準 FastAPI MVC 架構

```
chatbot-server/
├── main.py                 # 應用程式入口點
├── requirements.txt        # Python 依賴套件
├── Dockerfile             # Docker 容器化配置
├── .env_example           # 環境變數範例
├── README.md              # 專案說明文件
├── config/                # 配置模組
│   ├── database.py        # MongoDB 資料庫配置
│   └── openai.py          # OpenAI API 配置
├── controllers/           # 控制器層 (API 端點)
│   ├── chat.py            # 聊天控制器
│   ├── document.py        # 文件控制器
│   └── embedding.py       # 嵌入控制器
├── services/              # 業務邏輯層
│   ├── chat.py            # 聊天服務
│   └── vector.py          # 向量資料庫服務
├── models/                # 資料模型層 (Database Models)
│   └── user.py            # 使用者模型
├── schemas/               # API 模型層 (Pydantic Schemas)
│   └── user.py            # 使用者請求和回應模型
├── routers/               # 路由配置
│   └── routers.py         # 路由整合
└── vector_store/          # 向量資料庫
```

## 🔧 技術棧

### 核心框架
- **FastAPI**: 現代化的 Python Web 框架
- **Uvicorn**: ASGI 伺服器
- **LangChain**: AI 應用開發框架

### 資料庫
- **MongoDB**: 使用 Motor (異步驅動) 和 Beanie (ODM)
- **ChromaDB**: 向量資料庫

### AI 服務
- **OpenAI**: GPT-4 聊天模型和 text-embedding-3-large 嵌入模型

## 📋 API 端點

### 聊天功能 (`/chat`)
- `POST /chat/ask` - 發送問題並取得答案
- `GET /chat/user-status` - 取得使用者狀態
- `GET /chat/clean-chat-history` - 清理聊天歷史
- `POST /chat/reset-daily-count` - 重置每日計數 (管理員)

### 文件管理 (`/documents`)
- `POST /documents/merge-docs` - 合併文件

### 嵌入服務 (`/embedding`)
- `POST /embedding/create-embeddings` - 創建嵌入

## 🎯 主要改進

### 1. 標準化命名
- `qa_controller.py` → `chat.py`
- `qa_service.py` → `chat.py`
- `qa_model.py` → `user.py`
- `mongo_db.py` → `database.py`
- `open_ai.py` → `openai.py`
- `vector_store_service.py` → `vector.py`

### 2. 新增 Schemas 層
- 分離 API 請求和回應模型
- 使用 Pydantic 進行資料驗證
- 提供完整的 API 文檔

### 3. 模型優化
- 更清晰的欄位命名 (`user_email` → `email`)
- 添加時間戳記 (`created_at`, `updated_at`)
- 更好的錯誤處理和驗證
- 新增實用方法 (`to_dict`, `reset_daily_count`)

### 4. 控制器改進
- 使用標準 HTTP 狀態碼
- 統一的錯誤處理
- 完整的日誌記錄
- 類型提示和文檔字串

## 🚀 快速開始

### 1. 安裝依賴
```bash
# 創建虛擬環境
python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate     # Windows

# 安裝套件
pip install -r requirements.txt
```

### 2. 配置環境變數
```bash
cp .env_example .env
# 編輯 .env 檔案，填入必要的配置
```

### 3. 啟動服務
```bash
python3 main.py
```

### 4. 訪問 API 文檔
```
http://localhost:8000/docs
```

## 📊 資料模型

### User 模型
```python
class User(Document):
    email: EmailStr                    # 使用者郵箱
    questions_by_date: Dict[str, int]  # 每日問題計數
    is_admin: bool                     # 管理員權限
    created_at: datetime               # 創建時間
    updated_at: datetime               # 更新時間
```

## 🔒 權限管理

- **一般使用者**: 每日最多 10 個問題
- **管理員**: 無限制使用
- **管理員功能**: 重置使用者計數

## 🧪 API 測試

### 測試問答功能
```bash
curl -X POST "http://localhost:8000/chat/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "你好", "user_email": "test@example.com"}'
```

### 測試使用者狀態
```bash
curl -X GET "http://localhost:8000/chat/user-status?user_email=test@example.com"
```

### 測試清理聊天歷史
```bash
curl -X GET "http://localhost:8000/chat/clean-chat-history"
```

## 📝 開發指南

### 添加新的 API 端點
1. 在 `schemas/` 中定義請求和回應模型
2. 在 `controllers/` 中實現控制器邏輯
3. 在 `routers/routers.py` 中註冊路由

### 添加新的資料模型
1. 在 `models/` 中定義 Beanie 模型
2. 在 `config/database.py` 中註冊模型
3. 在 `schemas/` 中定義對應的 API 模型

## 🐳 Docker 部署

```bash
docker build -t langchain-chatbot .
docker run -p 8000:8000 langchain-chatbot
```

## 🔧 故障排除

### 端口衝突
如果遇到端口衝突，可以修改 `main.py` 中的端口設定：
```python
uvicorn.run(app, host="0.0.0.0", port=8000)  # 改為其他端口
```

### 環境變數
確保 `.env` 檔案包含所有必要的配置：
- `OPENAI_API_KEY`
- `OPENAI_MODEL`
- `EMBEDDING_MODEL`
- `MONGO_URI`
- `DATABASE_NAME`
- `ADMIN_USER`

## 📄 授權

本專案採用 MIT 授權條款。 