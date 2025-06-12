# Telegram Analyzer with AI (Gemini)

A Python tool that connects to your Telegram account (via Telethon), reads messages from a chat or channel,  
and sends them to a Google-powered generative AI for analysis.

---


## Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Versions](#versions)  
4. [Requirements](#requirements)  
   - [Environment Setup](#environment-setup)  
5. [Installation & Usage](#installation--usage)  

---

## Features

- Authenticate to Telegram via [Telethon](https://docs.telethon.dev/).  
- Pull messages (history, new messages, etc.).  
- Call Google Generative AI to summarize or analyze text.  
- Output results to file.

## Project Structure
```text
task/
├── .env
├── src
│   ├── main.py   
│   ├── analyze.py   
│   ├── config.py  
│   ├── ai_analiz.py
│   └── get_date.py         
├── .gitignore                 
├── .env              
├── pyproject.toml            
└── README.md
```




## Versions

[Python](https://www.python.org): **3.13**
[Telethon](https://docs.telethon.dev/en/stable/#): **1.40**
[Google Generative AI](): **0.1.0**

## Requirements

---

1. Python 3.10+ installed on your system.  
2. A Telegram API app (API_ID & API_HASH).  
3. A Google Generative AI API key.  

## Installation & Usage
---

```
You must have on your local computer installed Python

```text
git clone https://github.com/your-username/telegram-analyzer-ai.git
cd telegram-analyzer-ai
```


Package manager
```text
pip install uv
```

Windows:
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:
```text
python3 -m venv venv
source venv/bin/activate
```

You need to install **pyproject.toml**:
```text
pip install pyproject.toml
```


### Environment Setup

---

1. Register a new app on Telegram → https://my.telegram.org/auth?to=apps  
   • Copy your **API_ID** and **API_HASH**.  
2. Sign up for Google Generative AI → https://aistudio.google.com/  
   • Copy your **AI_API_KEY**.  
3. In the project root, create a file named `.env` containing:

   ```dotenv
   API_ID=your_telegram_api_id
   API_HASH=your_telegram_api_hash
   AI_API_KEY=your_google_ai_api_key

Set your bot settings like this:
```text 
API_ID=<your-telegram-api_token>
API_HASH=<your-telegram-api-hash>
AI_API_KEY=<your-api_ai>
```

4.Your .env file should look like this:
```text 
API_ID=<your-telegram-api_token>
API_HASH=<your-telegram-api-hash>
AI_API_KEY=<your-api_ai>

```




##Running the Project

```text 
python src/main.py
```
or
```text 
uv run src/main.py
```
