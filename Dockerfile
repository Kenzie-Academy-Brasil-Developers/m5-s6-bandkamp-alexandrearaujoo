FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]