if [ "$DJANGO_ENV" = "production" ]; then
    exec gunicorn --bind 0.0.0.0:$PORT project.wsgi --threads=2 --workers=3 --timeout 60
else
    exec gunicorn --bind 0.0.0.0:$PORT project.wsgi --reload --log-level error
fi
