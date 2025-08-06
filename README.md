# LangChain-WebUI

## 🚀 Project Introduction

LangChain-WebUI is a powerful chatbot generator and management platform. It allows users to quickly create and deploy customized chatbots based on LangChain through a simple configuration interface.

### ✨ Core Features

- **🎯 One-Click Generation**: Quickly generate complete chatbots through Web UI configuration
- **📚 Knowledge Base Management**: Support Markdown files as knowledge base
- **🐳 Docker Containerization**: Automatically generate Docker containers for easy deployment
- **🎛️ Unified Management**: Centralized management of all generated chatbot services
- **🔧 Customizable Configuration**: Support custom bot names, descriptions, and functionality
- **🤖 AI-Powered Chat**: Advanced conversational AI with context awareness
- **👥 User Management**: Role-based access control and usage tracking

### 🏗️ Architecture Overview

```
LangChain-WebUI (Control Panel)
├── Chatbot Configuration Interface
├── Knowledge Base Upload Management
├── Bot Generation Engine
└── Container Management System
    ├── ChatBot-1 (Container)
    ├── ChatBot-2 (Container)
    └── ChatBot-N (Container)
```

## 🎯 Usage Workflow

### 1. Create New Chatbot
1. Fill in bot configuration in Web UI:
   - Bot name
   - Bot description
   - API key configuration
2. Upload Markdown files as knowledge base
3. Click "Build & Export" button

### 2. Automatic Generation
The system will automatically:
- Generate complete chatbot code
- Create Docker container configuration
- Set up necessary environment variables
- Deploy to independent containers

### 3. Service Management
- View all running chatbots
- Start/stop/restart services
- Monitor service status
- View logs and statistics

## 🛠️ Technical Architecture

### Frontend (React + TypeScript)
```
chatbot-gui/
├── src/
│   ├── components/
│   │   ├── BotCreator/          # Bot creation interface
│   │   ├── BotManager/          # Bot management interface
│   │   ├── KnowledgeBase/       # Knowledge base management
│   │   └── Dashboard/           # Control panel dashboard
│   ├── services/
│   │   ├── botService.ts        # Bot service API
│   │   └── containerService.ts  # Container management API
│   └── types/
│       └── bot.ts              # Type definitions
```

### Backend (FastAPI + Python) - Optimized Architecture
```
chatbot-server/
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── config/                      # Configuration modules
│   ├── database.py             # MongoDB configuration
│   └── openai.py               # OpenAI API configuration
├── controllers/                 # Controller layer (API endpoints)
│   ├── chat.py                 # Chat controller
│   ├── document.py             # Document controller
│   └── embedding.py            # Embedding controller
├── services/                    # Business logic layer
│   ├── chat.py                 # Chat service
│   └── vector.py               # Vector database service
├── models/                      # Data model layer (Database Models)
│   └── user.py                 # User model
├── schemas/                     # API model layer (Pydantic Schemas)
│   └── user.py                 # User request/response models
├── routers/                     # Route configuration
│   └── routers.py              # Route integration
└── vector_store/               # Vector database
```

## 🚀 Quick Start

### Requirements
- Docker & Docker Compose
- Node.js 16+
- Python 3.8+

### Installation Steps

1. **Clone the project**
```bash
git clone https://github.com/pong1013/LangChain-WebUI.git
cd LangChain-WebUI
```

2. **Configure environment variables**
```bash
cp chatbot-server/.env_example chatbot-server/.env
# Edit .env file with your API keys
```

3. **Start services**
```bash
docker-compose up -d --build
```

4. **Access Web UI**
```
http://localhost:3000
```

### Manual Setup (Development)

1. **Setup Backend**
```bash
cd chatbot-server
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python3 main.py
```

2. **Setup Frontend**
```bash
cd chatbot-gui
npm install
npm start
```

## 📋 Configuration Guide

### Bot Configuration (.env_example)
```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4
EMBEDDING_MODEL=text-embedding-3-large

# Database Configuration
MONGO_URI=your_mongodb_uri
DATABASE_NAME=ChatBotDB

# Bot Configuration
BOT_NAME=My Custom Bot
BOT_DESCRIPTION=A helpful assistant for my documents
ADMIN_USER=admin@example.com
```

### Knowledge Base Files
- Support Markdown (.md) format
- Automatic processing of file structure and links
- Support for images and tables

## 🧪 API Testing

### Test Chatbot API
```bash
# Test question answering
curl -X POST "http://localhost:8000/chat/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "你好", "user_email": "test@example.com"}'

# Test user status
curl -X GET "http://localhost:8000/chat/user-status?user_email=test@example.com"

# Test clean chat history
curl -X GET "http://localhost:8000/chat/clean-chat-history"
```

### API Documentation
```
http://localhost:8000/docs
```

## 🎯 Recent Improvements

### Backend Architecture Optimization
- ✅ **Standardized Naming**: Consistent file naming convention
- ✅ **MVC Architecture**: Clear separation of concerns
- ✅ **Schema Layer**: Pydantic models for API validation
- ✅ **Error Handling**: Comprehensive error management
- ✅ **Type Safety**: Full type hints and validation
- ✅ **Documentation**: Complete API documentation

### Key Features
- **User Management**: Role-based access control
- **Usage Tracking**: Daily question limits and analytics
- **Vector Search**: Advanced knowledge base retrieval
- **Conversation History**: Context-aware conversations
- **Admin Controls**: Administrative functions and monitoring

## 🎯 Future Goals

### Phase 1: Basic Features ✅
- [x] **Web UI Interface**: Complete bot creation and management interface
- [x] **Template System**: Multiple preset bot templates
- [x] **Knowledge Base Processing**: Support for multiple file formats
- [x] **Container Management**: Basic Docker container lifecycle management
- [x] **API Architecture**: Optimized FastAPI backend structure

### Phase 2: Advanced Features
- [ ] **Multi-Model Support**: GPT-4, Claude, Gemini, etc.
- [ ] **Plugin System**: Extensible plugin architecture
- [ ] **Version Management**: Bot version control and rollback
- [ ] **Performance Monitoring**: Real-time performance monitoring and alerts

### Phase 3: Enterprise Features
- [ ] **Multi-Tenant Support**: Enterprise-level multi-user management
- [ ] **API Gateway**: Unified API access control
- [ ] **Backup & Recovery**: Automatic backup and disaster recovery
- [ ] **Audit Logging**: Complete operation audit records

### Phase 4: Intelligence
- [ ] **Auto-Optimization**: Model optimization based on usage data
- [ ] **Smart Routing**: Automatic selection of best models
- [ ] **A/B Testing**: Bot performance comparison testing
- [ ] **Predictive Analytics**: Usage trend prediction and capacity planning

## 🤝 Contributing
We welcome all forms of contributions!

### Development Environment Setup
1. Fork this project
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push branch: `git push origin feature/AmazingFeature`
5. Open Pull Request

### Contribution Types
- 🐛 Bug fixes
- ✨ New feature development
- 📚 Documentation improvements
- 🎨 UI/UX optimization
- ⚡ Performance optimization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact Us

- 🌐 Project Website: [https://langchain-webui.com](https://langchain-webui.com)
- 📧 Email: [pong861013@gmail.com](mailto:pong861013@gmail.com)
- 💬 Discord: [Join our community](https://discord.gg/langchain-webui)
- 🐛 Issues: [GitHub Issues](https://github.com/pong1013/LangChain-WebUI/issues)

---

## 🎉 Acknowledgments

Thanks to all developers and users who have contributed to this project!

---

*LangChain-WebUI - Making it easy for everyone to create their own AI chatbots* 🤖✨
