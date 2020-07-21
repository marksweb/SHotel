FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv

RUN mkdir /backend
WORKDIR /backend

ADD Pipfile Pipfile.lock /backend/
RUN pipenv install --dev

ADD . /backend/
