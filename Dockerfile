FROM python:3.8.12

WORKDIR /app
COPY . /app

ENV PYTHONUNBUFFERED=1

RUN pip3 install -U pipenv &&  \
    pipenv update &&  \
    pipenv install --system
