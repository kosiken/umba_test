FROM python:3.9 as base
RUN apt-get update && apt-get install python3-dev build-essential -y
WORKDIR /usr/src/app
COPY / .
RUN pip install gunicorn
RUN pip install -r requirements.txt

FROM base as production
RUN touch .env
RUN mv wsgi.txt wsgi.py

EXPOSE 3003

CMD ['./initdb.sh']
CMD exec gunicorn --bind :3003 --workers 3 --threads 8 wsgi:app

