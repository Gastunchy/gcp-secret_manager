# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY main.py .
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 8080

# Comando para ejecutar el script
CMD ["python", "main.py"]