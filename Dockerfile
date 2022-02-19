FROM python:3.10.2-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc postgresql netcat \
    && apt-get clean

# Install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

# copy entrypoint.sh
COPY ./entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

COPY . /code/

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
