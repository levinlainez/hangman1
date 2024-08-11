FROM python:3.9-slim

WORKDIR /app

# Instalar las dependencias necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "hangman/manage.py", "runserver", "0.0.0.0:8000"]
