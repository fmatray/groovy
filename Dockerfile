FROM python:3
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y vim

ENV PYTHONUNBUFFERED 1
RUN mkdir /groovy
WORKDIR /groovy
ADD requirements.txt /groovy/
RUN pip install -r requirements.txt
ADD . /groovy/
