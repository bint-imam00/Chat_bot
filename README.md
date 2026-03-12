# 🤖 AI Chatbot — Python · Flask · Docker · NLP

> **Built with Python · Flask · Docker · HTML**  
> A production-ready AI chatbot with REST API, custom ML models, and containerized deployment.

---

## ✨ Features

- **💬 Conversational AI** — Natural language understanding and context-aware responses
- **🔌 REST API** — Clean API endpoints for easy integration into any app or website
- **🧠 Custom ML Models** — Trained models stored and served from the `models/` directory
- **🐳 Docker Ready** — One-command deployment with included Dockerfile
- **🌐 Web Interface** — HTML frontend via Flask templates
- **📊 Data Pipeline** — Structured data processing in the `scripts/` folder

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| AI / NLP | Custom ML Models |
| Frontend | HTML + Flask Templates |
| Deployment | Docker |
| API | REST (JSON) |

---

## 📂 Project Structure

```
Chat_bot/
│
├── api/            # REST API routes & endpoints
├── data/           # Training & reference data
├── models/         # Trained ML models
├── scripts/        # Data processing & training scripts
├── templates/      # HTML frontend templates
├── Dockerfile      # Container configuration
├── requirements.txt
└── .gitignore
```

---

## ⚡ Quick Start

### Option 1 — Run with Docker (recommended)
```bash
git clone https://github.com/bint-imam00/Chat_bot.git
cd Chat_bot
docker build -t chatbot .
docker run -p 5000:5000 chatbot
```

### Option 2 — Run locally
```bash
git clone https://github.com/bint-imam00/Chat_bot.git
cd Chat_bot
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000`

---

## 🔌 API Usage

```bash
POST /api/chat
Content-Type: application/json

{
  "message": "Hello, how can you help me?"
}
```

**Response:**
```json
{
  "response": "Hi! I'm here to help. What do you need?",
  "confidence": 0.94
}
```

---

## 💡 Use Cases

This chatbot is adaptable for:
- 🏢 Customer support automation
- 🎓 Educational Q&A assistants
- 🏥 Healthcare FAQ bots
- 🌍 Multilingual African market applications

---

## 👩🏾‍💻 Author

**Aïcha Mbaye** — AI & Data Science Developer  
CTO @ Art'beau-rescence | Big Data Graduate, Dakar Institute of Technology  
📍 Dakar, Senegal

> Available for freelance missions in AI chatbot development, NLP, and Python API development.  
> 🔗 [GitHub Profile](https://github.com/bint-imam00)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
