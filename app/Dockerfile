# Dockerfile

FROM python:3.9

# Встановлення залежностей
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && pip install --upgrade pip

# Встановлення бібліотек Python
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Копіюємо код у контейнер
COPY . /app/

# Налаштування порту
EXPOSE 8000

# Команда для запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
