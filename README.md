# Install

> ###npm install

> ###npm run build

> ###pipenv install --dev && pipenv shell

> ###rename env.txt to .env

# Up development server

- ##run python dev server

> ###python manage.py runserver

- ##run celery worker for download files

> ###celery -A backend.settings.celery multi start worker1 --loglevel=INFO --concurrency=3 --logfile="/home/u/uicode/admin.med-market.rf/med_market/log/%n%I.log" --pidfile="/home/u/uicode/admin.med-market.rf/med_market/log/%n.pid"

- ## development celery

> ###celery -A backend.settings.celery worker --loglevel=INFO --concurrency=3 -P gevent

- ##run vue dev server

> ###npm run serve
