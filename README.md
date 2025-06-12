# Telegram Analyzer з AI (Gemini)

Цей проєкт аналізує переписки менеджерів з клієнтами в Telegram, виявляючи:
- 📌 Невиконані обіцянки (наприклад: "зроблю до кінця дня", але не зробив)
- 😠 Проблемні діалоги з емоційним або негативним тоном
- 📊 Основні метрики по роботі менеджерів

---

### ✅ Основні можливості:
1. **Збір діалогів** з Telegram через Telethon API
2. **Збереження в `chats_data.json`** у структурованому вигляді
3. **AI-аналіз** кожного діалогу через [Gemini 1.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/overview)
4. **Збереження результатів у `ai_logs.txt`** у зручному форматі



## Requirements

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

```
## Versions

[Python](https://www.python.org): **3.13**
[Telethon](https://docs.telethon.dev/en/stable/#): **1.40**
[Google Generative AI](): **0.1.0**



### Env Setup


---



To set up a project, you need a create ".env"
file in main directory and fill it with the following data:

 - Register on: https://my.telegram.org/auth?to=apps 
 - Create app for API_HASH, API_ID
 - Get GOOGLE_API_KEY from https://aistudio.google.com/.

Set your bot settings like this:

TELEGRAM_API_HASH=<your-telegram-api-hash>
TELEGRAM_API_ID=<your-telegram-api_token>
AI_API_KEY=<your-api_ai>

Set it in the same file.
Your .env file should look like this:
text


TELEGRAM_API_ID=<your-telegram-api-id>
TELEGRAM_API_HASH=<your-telegram-api-hash>

GOOGLE_API_KEY=<your-google-api-key>

