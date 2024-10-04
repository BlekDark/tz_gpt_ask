Этот проект реализует взаимодействие с сервисом GigaChat, где пользователь может общаться с моделью, настроенной под определённый контекст.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:BlekDark/tz_gpt_ask.git

2. В .env пропишите GIGACHAT_API_KEY и GIGACHAT_SCOPE

3. Сборка docker образа:
   ```bash
   docker build -t gigachat-script .
   
   docker run -it --env-file .env gigachat-script

   
