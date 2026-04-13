#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Improved Superuser Script
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='soham').exists():
    User.objects.create_superuser('soham', 'sharma.soham04@gmail.com', 'admin')
    print("Superuser 'soham' created successfully.")
else:
    print("Superuser 'soham' already exists.")
END