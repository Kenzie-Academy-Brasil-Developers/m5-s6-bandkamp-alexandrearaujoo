FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt .

RUN pip install -r requirement.txt

WORKDIR /code

COPY . /code/