FROM python:3.8.3-slim

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && \
    apt-get -y install libpq-dev gcc && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    /py/bin/pip install -r /tmp/requirements.dev.txt && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"
