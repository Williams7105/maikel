#!/usr/bin/env bash
set -o errexit

# Instala dependencias
pip install -r requirements.txt

# Recolecta archivos estáticos
python manage.py collectstatic --noinput

# Aplica migraciones
python manage.py migrate