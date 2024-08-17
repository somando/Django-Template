FROM python

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN apt-get update && apt-get install -y postgresql-client
RUN pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn

CMD [ "gunicorn", "config.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock" ]
