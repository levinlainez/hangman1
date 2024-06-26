# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt en el contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto en el contenedor
COPY . .

# Expone el puerto que Django usará
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "hangman/manage.py", "runserver", "0.0.0.0:8000"]
