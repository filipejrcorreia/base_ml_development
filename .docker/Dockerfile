#FROM python:3.6
FROM nvidia/cuda:11.3.0-cudnn8-runtime-ubuntu20.04
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.6 \
    python3-pip \
    && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*
ADD ./dependencies /dependencies
WORKDIR /dependencies
RUN pip install --upgrade pip
RUN pip install wheel  
RUN pip install -r requirements.txt
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
RUN mkdir /data
RUN mkdir /data/jupyter
RUN mkdir /data/jupyter/datasets
RUN mkdir /git
RUN mkdir /git/python_modules
RUN mkdir /opt/ssl-certs
RUN mkdir /opt/ssl-certs/jupyter
VOLUME /data/jupyter
VOLUME /data/jupyter/datasets
VOLUME /git/python_modules
VOLUME /opt/ssl-certs/jupyter
COPY /dependencies/start-notebook.sh /usr/local/bin
COPY /opt/ssl-certs/jupyter/jupyter.pem /etc/ssl/notebook/jupyter.pem

