# Используем базовый образ Python
FROM python:3.10

# Копируем файлы в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем российские сертификаты
RUN gigachain install-rus-certs || echo "Ошибка установки сертификатов, продолжаем без них."

# Запуск программы
CMD ["python", "main.py"]