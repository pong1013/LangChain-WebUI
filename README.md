# LangChain-WebUI

## 🚀 專案介紹

LangChain-WebUI 是一個強大的聊天機器人生成器和管理平台。它允許用戶通過簡單的配置界面，快速創建和部署基於 LangChain 的客製化聊天機器人。

### ✨ 核心功能

- **🎯 一鍵生成**: 通過 Web UI 配置，快速生成完整的聊天機器人
- **📚 知識庫管理**: 支援 Markdown 文件作為知識庫
- **🐳 Docker 容器化**: 自動生成 Docker 容器，便於部署
- **🎛️ 統一管理**: 集中管理所有生成的聊天機器人服務
- **🔧 客製化配置**: 支援自定義機器人名稱、描述和功能

### 🏗️ 架構概覽

```
LangChain-WebUI (主控台)
├── 聊天機器人配置界面
├── 知識庫上傳管理
├── 機器人生成引擎
└── 容器管理系統
    ├── ChatBot-1 (Container)
    ├── ChatBot-2 (Container)
    └── ChatBot-N (Container)
```

## 🎯 使用流程

### 1. 創建新聊天機器人
1. 在 Web UI 中填寫機器人配置：
   - 機器人名稱
   - 機器人描述
   - API 金鑰配置
2. 上傳 Markdown 文件作為知識庫
3. 點擊 "Build & Export" 按鈕

### 2. 自動生成
系統會自動：
- 生成完整的聊天機器人代碼
- 創建 Docker 容器配置
- 設置必要的環境變數
- 部署到獨立的容器中

### 3. 管理服務
- 查看所有運行中的聊天機器人
- 啟動/停止/重啟服務
- 監控服務狀態
- 查看日誌和統計

## 🛠️ 技術架構

### 前端 (React + TypeScript)
```
chatbot-gui/
├── src/
│   ├── components/
│   │   ├── BotCreator/          # 機器人創建界面
│   │   ├── BotManager/          # 機器人管理界面
│   │   ├── KnowledgeBase/       # 知識庫管理
│   │   └── Dashboard/           # 主控台儀表板
│   ├── services/
│   │   ├── botService.ts        # 機器人服務 API
│   │   └── containerService.ts  # 容器管理 API
│   └── types/
│       └── bot.ts              # 類型定義
```

### 後端 (FastAPI + Python)
```
chatbot-server/
├── api/
│   ├── bot_creator.py          # 機器人生成 API
│   ├── container_manager.py    # 容器管理 API
│   └── knowledge_base.py       # 知識庫管理 API
├── generators/
│   ├── bot_generator.py        # 機器人代碼生成器
│   ├── docker_generator.py     # Docker 配置生成器
│   └── template_engine.py      # 模板引擎
├── services/
│   ├── container_service.py    # Docker 容器服務
│   └── file_service.py         # 文件管理服務
└── templates/
    ├── bot_template/           # 機器人模板
    └── docker_template/        # Docker 模板
```

## 🚀 快速開始

### 環境要求
- Docker & Docker Compose
- Node.js 16+
- Python 3.8+

### 安裝步驟

1. **克隆專案**
```bash
git clone https://github.com/your-username/LangChain-WebUI.git
cd LangChain-WebUI
```

2. **配置環境變數**
```bash
cp chatbot-server/.env_example chatbot-server/.env
# 編輯 .env 文件，填入您的 API 金鑰
```

3. **啟動服務**
```bash
docker-compose up -d --build
```

4. **訪問 Web UI**
```
http://localhost:3000
```

## 📋 配置說明

### 機器人配置 (.env_example)
```env
# OpenAI 配置
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4
EMBEDDING_MODEL=text-embedding-ada-002

# 資料庫配置
MONGO_URI=your_mongodb_uri
DATABASE_NAME=ChatBotDB

# 機器人配置
BOT_NAME=My Custom Bot
BOT_DESCRIPTION=A helpful assistant for my documents
ADMIN_USER=admin@example.com
```

### 知識庫文件
- 支援 Markdown (.md) 格式
- 自動處理文件結構和連結
- 支援圖片和表格

## 🎯 未來目標

### Phase 1: 基礎功能 (Q1 2024)
- [ ] **Web UI 界面**: 完整的機器人創建和管理界面
- [ ] **模板系統**: 預設多種機器人模板
- [ ] **知識庫處理**: 支援多種文件格式
- [ ] **容器管理**: 基本的 Docker 容器生命週期管理

### Phase 2: 進階功能 (Q2 2024)
- [ ] **多模型支援**: GPT-4, Claude, Gemini 等
- [ ] **插件系統**: 可擴展的插件架構
- [ ] **版本管理**: 機器人版本控制和回滾
- [ ] **性能監控**: 實時性能監控和警報

### Phase 3: 企業功能 (Q3 2024)
- [ ] **多租戶支援**: 企業級多用戶管理
- [ ] **API 網關**: 統一的 API 訪問控制
- [ ] **備份恢復**: 自動備份和災難恢復
- [ ] **審計日誌**: 完整的操作審計記錄

### Phase 4: 智能化 (Q4 2024)
- [ ] **自動優化**: 基於使用數據的模型優化
- [ ] **智能路由**: 自動選擇最佳模型
- [ ] **A/B 測試**: 機器人性能對比測試
- [ ] **預測分析**: 使用趨勢預測和容量規劃

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

### 開發環境設置
1. Fork 本專案
2. 創建功能分支: `git checkout -b feature/AmazingFeature`
3. 提交更改: `git commit -m 'Add AmazingFeature'`
4. 推送分支: `git push origin feature/AmazingFeature`
5. 開啟 Pull Request

### 貢獻類型
- 🐛 Bug 修復
- ✨ 新功能開發
- 📚 文檔改進
- 🎨 UI/UX 優化
- ⚡ 性能優化

## 📄 授權

本專案採用 MIT 授權 - 查看 [LICENSE](LICENSE) 文件了解詳情。

## 📞 聯繫我們

- 🌐 專案網站: [https://langchain-webui.com](https://langchain-webui.com)
- 📧 郵箱: [your-email@example.com](mailto:your-email@example.com)
- 💬 Discord: [加入我們的社群](https://discord.gg/langchain-webui)
- 🐛 Issues: [GitHub Issues](https://github.com/your-username/LangChain-WebUI/issues)

---

## 🎉 致謝

感謝所有為這個專案做出貢獻的開發者和用戶！

---

*LangChain-WebUI - 讓每個人都能輕鬆創建自己的 AI 聊天機器人* 🤖✨
