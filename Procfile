heroku ps:scale worker=1
release: python manage.py migrate
web: daphne LineMaroBack.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python3 manage.py runworker channel_layers --settings=LineMaroBack.settings -v2
