FROM python:3.8-slim AS base

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0

COPY Pipfile .
RUN pip install pipenv

FROM base AS dependencies
RUN pipenv install --system --skip-lock

FROM base AS development
RUN pipenv install --system --dev --skip-lock
COPY . .

FROM dependencies AS production
COPY app app
COPY run.py .