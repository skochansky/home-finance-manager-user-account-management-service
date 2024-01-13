FROM python:3.12
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY . /app

RUN pip3 install poetry && poetry install --no-cache

ENTRYPOINT [".docker/entrypoint.sh"]
