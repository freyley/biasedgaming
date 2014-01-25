#web: newrelic-admin run-program python biasedgaming/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 5
web: newrelic-admin run-program gunicorn biasedgaming/biasedgaming/wsgi.py -b "0.0.0.0:$PORT" -w 5
