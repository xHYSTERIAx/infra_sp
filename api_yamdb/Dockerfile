FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]

ENV SECRET_KEY 'p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'