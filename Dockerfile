# UniversalTranslator:1.0
#FROM debian
FROM python:3
MAINTAINER TEST <placeholder@mail.local>
WORKDIR /app
copy requirements.txt requirements.txt
copy frontend frontend
copy main.py main.py
#RUN apt-get update
#RUN apt-get -y install python3
#RUN apt-get -y install python3-pip
RUN pip3 install -r ./requirements.txt

#docker build -t universaltranslator:1.0 ./


