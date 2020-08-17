FROM python:3.8-slim

COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "main.py"]