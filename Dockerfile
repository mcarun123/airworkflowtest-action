
FROM python:3.7
RUN mkdir /src
COPY /src /src
COPY pyproject.toml /src
COPY poetry.lock /src
WORKDIR /src
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
#CMD ["/src/run.py","$INPUT_TYPE","$INPUT_FUNCTION"]

