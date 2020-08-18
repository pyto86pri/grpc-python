FROM python:3.8-slim

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY . .
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "main.py"]