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

# Establece el directorio de trabajo en el contenedor
WORKDIR /code

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto a /code
COPY . .

# Expone el puerto 8002 para la aplicación Django
EXPOSE 8002

# Ejecuta el script de comandos al iniciar el contenedor
ENTRYPOINT ["./command.sh"]
