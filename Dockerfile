FROM python:3
LABEL maintainer="alexandro@autistici.org"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD Form/ /code/