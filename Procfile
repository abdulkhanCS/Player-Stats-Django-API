release: python src.manage.py makemigrations --no-input
release: python src.manage.py migrate --no-input

web: gunicorn src.core.views