FROM python:3.12.10-alpine3.21

COPY ./app /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip

ENV PATH="/py/bin:$PATH"

CMD ["python", "main.py"]
