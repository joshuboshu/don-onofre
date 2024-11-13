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

# Copia todo el contenido del proyecto a /app
COPY . .

# Instala dependencias de Python
RUN pip install -r requirements.txt

# Define el comando de inicio del contenedor
CMD ["sh", "./command.sh"]
