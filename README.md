# Astrox: Reverse Thinking AI Chatbot

Astrox is a sleek, terminal-inspired Flask web application that leverages the **Groq API** (Llama 3.3-70B) to provide users with structured, step-by-step guidance to achieve their goals. The system is designed with a "Reverse Thinking" logic, helping users break down complex objectives into manageable, actionable steps.

## 🚀 Features

- **AI-Powered Reasoning:** Uses the `llama-3.3-70b-versatile` model via Groq for high-speed, intelligent responses.
- **Cyber-Terminal UI:** A dark-themed, high-contrast interface featuring a "Hacker" aesthetic with green glow effects and terminal fonts.
- **Structured Outputs:** The AI is system-prompted to provide answers in a clear, numbered, step-by-step format.
- **Secure Integration:** Utilizes environment variables for API key management and Flask session security.
- **Responsive Design:** Optimized for both desktop and mobile viewing with CSS-driven animations.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI Integration:** Groq SDK (Llama 3.3 Model)
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Environment Management:** `python-dotenv`

## 📋 Prerequisites

Before running the application, ensure you have:
- Python 3.8 or higher installed.
- A **Groq API Key** (Obtainable from [Groq Cloud](https://console.groq.com/)).

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/astrox-chatbot.git](https://github.com/your-username/astrox-chatbot.git)
   cd astrox-chatbot