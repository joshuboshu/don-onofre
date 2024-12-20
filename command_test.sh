#!/bin/bash

# Baja los contenedores en caso de que ya estén corriendo
sudo docker compose down

# Construye las imágenes de los servicios
sudo docker compose build

# Levanta los servicios en segundo plano
sudo docker compose up -d

# Espera unos segundos para asegurarse de que el contenedor de la base de datos esté listo
sleep 10

# Ejecuta makemigrations y migrate
sudo docker compose exec web python manage.py makemigrations
sudo docker compose exec web python manage.py migrate

# Abre automáticamente en el navegador la aplicación de pruebas (asegúrate de que coincida el puerto con .env.test)
if command -v xdg-open &> /dev/null; then
    xdg-open http://192.168.100.153:8002
elif command -v open &> /dev/null; then
    open http://192.168.100.153:8002
fi
