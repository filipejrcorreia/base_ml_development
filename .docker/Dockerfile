FROM python:3.11.1-alpine
RUN apk update && apk upgrade
RUN apk add make automake gcc g++ subversion gfortran libpng-dev python3-dev
ADD . /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt