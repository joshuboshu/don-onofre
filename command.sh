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

# Abre automáticamente en el navegador (asegúrate de que coincida el puerto con docker-compose)
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:8002
elif command -v open &> /dev/null; then
    open http://localhost:8002
fi