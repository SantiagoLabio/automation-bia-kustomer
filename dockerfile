# Utilizar una imagen base ligera de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo .env al contenedor
COPY .env /app/.env

# Copiar los archivos requirements.txt para instalar dependencias
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido de la aplicación a la imagen
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación (8000 es el puerto por defecto de FastAPI)
EXPOSE 8000

# Comando para correr la aplicación usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "2181"]
