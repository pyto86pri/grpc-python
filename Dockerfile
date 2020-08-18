FROM python:3.8-slim

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY poetry.lock pyproject.toml ./
RUN poetry install
COPY ./src .

ENTRYPOINT ["poetry", "run", "python", "main.py"]