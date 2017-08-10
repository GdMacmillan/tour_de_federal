web: gunicorn --pythonpath tdf_site tdf_site.wsgi collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT tdf_site/settings.py 
