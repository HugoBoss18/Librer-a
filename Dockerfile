#Dockerfile
FROM python:3.13-slim-trixie

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requerimientos.txt .
RUN pip install --no-cache-dir --upgrade -r requerimientos.txt

COPY . .