# Usa la imagen base de Python
FROM python:3.10-alpine

# Instala dependencias necesarias
RUN apk update && apk add --no-cache \
    libpq-dev \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido del proyecto
COPY . .

# Da permisos de ejecución al script .sh
RUN chmod +x tu_script.sh

# Ejecuta el script .sh al iniciar el contenedor
CMD ["sh", "/app/command.sh"]