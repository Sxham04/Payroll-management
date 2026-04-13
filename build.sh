#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

if [ "$CREATE_SUPERUSER" ]; then
  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='soham').exists() or User.objects.create_superuser('soham', 'sharma.soham04@gmail.com', 'admin')"
fi