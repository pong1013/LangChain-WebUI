# LangChain-WebUI

## 🚀 Project Introduction

LangChain-WebUI is a powerful chatbot generator and management platform. It allows users to quickly create and deploy customized chatbots based on LangChain through a simple configuration interface.

### ✨ Core Features

- **🎯 One-Click Generation**: Quickly generate complete chatbots through Web UI configuration
- **📚 Knowledge Base Management**: Support Markdown files as knowledge base
- **🐳 Docker Containerization**: Automatically generate Docker containers for easy deployment
- **🎛️ Unified Management**: Centralized management of all generated chatbot services
- **🔧 Customizable Configuration**: Support custom bot names, descriptions, and functionality

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

### Backend (FastAPI + Python)
```
chatbot-server/
├── api/
│   ├── bot_creator.py          # Bot generation API
│   ├── container_manager.py    # Container management API
│   └── knowledge_base.py       # Knowledge base management API
├── generators/
│   ├── bot_generator.py        # Bot code generator
│   ├── docker_generator.py     # Docker configuration generator
│   └── template_engine.py      # Template engine
├── services/
│   ├── container_service.py    # Docker container service
│   └── file_service.py         # File management service
└── templates/
    ├── bot_template/           # Bot templates
    └── docker_template/        # Docker templates
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

## 📋 Configuration Guide

### Bot Configuration (.env_example)
```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4
EMBEDDING_MODEL=text-embedding-ada-002

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

## 🎯 Future Goals

### Phase 1: Basic Features
- [ ] **Web UI Interface**: Complete bot creation and management interface
- [ ] **Template System**: Multiple preset bot templates
- [ ] **Knowledge Base Processing**: Support for multiple file formats
- [ ] **Container Management**: Basic Docker container lifecycle management

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
