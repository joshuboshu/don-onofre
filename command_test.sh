#!/bin/bash

# Baja los contenedores de pruebas en caso de que ya estén corriendo
docker compose -f docker-compose.test.yml down

# Construye las imágenes de los servicios de pruebas
docker compose -f docker-compose.test.yml build

# Levanta los servicios de pruebas en segundo plano
docker compose -f docker-compose.test.yml up -d

# Espera unos segundos para asegurarse de que el contenedor de la base de datos de pruebas esté listo
sleep 10

# Ejecuta makemigrations y migrate en el entorno de pruebas
docker compose -f docker-compose.test.yml exec web_test python manage.py makemigrations
docker compose -f docker-compose.test.yml exec web_test python manage.py migrate

# Abre automáticamente en el navegador la aplicación de pruebas (asegúrate de que coincida el puerto con .env.test)
if command -v xdg-open &> /dev/null; then
    xdg-open http://192.168.100.153:8002
elif command -v open &> /dev/null; then
    open http://192.168.100.153:8002
fi
