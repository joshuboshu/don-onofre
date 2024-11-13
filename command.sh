#!/bin/bash

# Detiene y elimina contenedores, redes y volúmenes anteriores
docker compose down --volumes --remove-orphans

# Construye los contenedores
docker compose build

# Levanta los contenedores
docker compose up --remove-orphans -d

# Instala dependencias de Python en el contenedor 'web'
docker compose exec web pip install -r requirements.txt

# Aplica las migraciones de Django
docker compose exec web python manage.py migrate

# Ejecuta collectstatic de Django
docker compose exec web python manage.py collectstatic --noinput

# Inicia el servidor de Django
docker compose exec web python manage.py runserver 0.0.0.0:8000

# Muestra los logs de los contenedores
docker compose logs -f
