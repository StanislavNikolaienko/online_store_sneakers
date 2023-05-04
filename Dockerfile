FROM python:3.11

ARG sneakers

ENV sneakers=${sneakers}\
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.4.2

RUN pip install "poetry==$POETRY_VERSION"
WORKDIR ./python_docker
COPY poetry.lock pyproject.toml  ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-dev

COPY . /python_docker

EXPOSE 8000
CMD ["python", "store/manage.py", "migrate"]
CMD ["python", "store/manage.py", "runserver", "0.0.0.0:8000"]
