FROM python:3.12

RUN mkdir /app
WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock /app/

# Allow installing dev dependencies to run tests
RUN poetry install --no-dev

COPY ./src/ /app/

EXPOSE 8008

CMD /app/start_app.sh
