FROM python:3.13-slim


RUN pip install poetry


WORKDIR /app

COPY pyproject.toml poetry.lock* /app/


RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app

WORKDIR /app/book_api
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
