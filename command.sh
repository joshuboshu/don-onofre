#!/bin/bash

# Detiene y elimina contenedores, redes y volúmenes anteriores
docker compose down --volumes --remove-orphans

# Construye los contenedores
docker compose build

# Levanta los contenedores en segundo plano
docker compose up --remove-orphans -d

# Instala dependencias de Python en el contenedor 'web' (por si hay cambios)
docker compose exec web pip install -r requirements.txt

# Aplica migraciones de Django
docker compose exec web python manage.py migrate

# Ejecuta collectstatic de Django sin intervención del usuario
docker compose exec web python manage.py collectstatic --noinput

# Inicia el servidor de Django en el puerto 8002
docker compose exec web python manage.py runserver 0.0.0.0:8002
