import json

def ai_analiz(model, chats):
         
    with open('ai_logs.txt', 'w', encoding='utf-8') as log_file:

        for chat in chats:
            chat_name = chat.get("chat_name")
            messages = chat.get("messages", [])
            if not messages:
                continue
            
            dialogue_text = "\n".join(messages)

            prompt = f"""
                    Ось переписка з клієнтом і менеджером:
                    {dialogue_text}
                    Запитання:
                    - Чи менеджер пообіцяв щось зробити до кінця дня?
                    - Якщо так, то чи виконав обіцянку?
                    - Якщо ні, чи потрібно звернути увагу на цей діалог як на проблему?

                    Зверни увагу на емоції, час відправи повідомлень, і чи були обіцянки виконані.
                    
                    Коли пишеш відповідь то пиши запитання та відповіді окремо, як в прикладі:
                    Запитання: Чи менеджер пообіцяв щось зробити до кінця дня?
                    Відповідь: Так, менеджер пообіцяв зробити X до кінця дня.

                    Відповідай коротко, чітко, структуровано.
                    """
            try:
                response = model.generate_content(prompt)
                result = response.text.strip()

                log_file.write(f"ЧАТ: {chat_name}\n")
                log_file.write(f"{result}\n")
                log_file.write("-" * 60 + "\n")

            except Exception as e:
                print(f"❌ Помилка в аналізі чату {chat_name}: {e}")
