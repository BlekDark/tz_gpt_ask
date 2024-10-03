import os
from dotenv import load_dotenv

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

load_dotenv()


api_key = os.getenv("GIGACHAT_API_KEY")
gigachat_scope = os.getenv("GIGACHAT_SCOPE")


# Авторизация в сервисе GigaChat
chat = GigaChat(credentials=api_key, scope=gigachat_scope)

messages = 0

gpt_array = ['gigachat']
while(True):
    print(f'Введите модель gpt. Сейчас доступны: {gpt_array}')
    gpt_input = input("Введите модель gpt: ")
    if gpt_input == 'exit':
        break
    if gpt_input in gpt_array:
        if gpt_input == 'gigachat':
            # Проверка на наличие контекста и его добавление
            print('Задайте контекст, в котором Вам будут отвечать. Например: '
                  '"Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."')
            input_context = input()
            messages = [
                SystemMessage(
                    content=input_context
                )
            ]
            while (True):
                # Ввод пользователя
                user_input = input("User: ")
                if user_input == 'exit':
                    break
                messages.append(HumanMessage(content=user_input))
                res = chat(messages)
                messages.append(res)
                # Ответ сервиса
                print("Bot: ", res.content)
    else:
        print('Такой модели нет, введите модель из списка')

print('Завершение работы программы')