#!/bin/bash

# Baja los contenedores en caso de que ya estén corriendo
docker compose down

# Construye las imágenes de los servicios
docker compose build

# Levanta los servicios en segundo plano
docker compose up -d

# Espera unos segundos para asegurarse de que el contenedor de la base de datos esté listo
sleep 10

# Ejecuta makemigrations y migrate
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

# Ejecuta el servidor de desarrollo
docker compose exec web python manage.py runserver 0.0.0.0:8002
