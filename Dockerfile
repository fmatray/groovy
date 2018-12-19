 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /groovy
 WORKDIR /groovy
 ADD requirements.txt /groovy/
 RUN pip install -r requirements.txt
 ADD . /groovy/
