# Usa la imagen base de Python
FROM python:3.12-alpine

# Configuración de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido del proyecto
COPY . .

# Da permisos de ejecución al script .sh
RUN chmod +x tu_script.sh

# Ejecuta el script .sh al iniciar el contenedor
CMD ["sh", "/app/command.sh"]