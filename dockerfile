# Usa una imagen base oficial de Python con versión específica
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia las dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el código fuente
COPY . .

# Cambia los permisos para que el usuario pueda ejecutar el código
RUN chmod -R 755 /app

# Establece PYTHONPATH para que Python encuentre los módulos
ENV PYTHONPATH=/app/Models:/app/Tienda\ Service:/app/Main

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "Main/main.py"]