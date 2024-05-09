FROM python:3.12


RUN apt-get update -yy
#RUN apt-get upgrade -yy
RUN apt install -yy \
    git

COPY . /home/ransomwatch
RUN mkdir /home/ransomwatch/source 

RUN pip3 install -r /home/ransomwatch/requirements.txt

RUN playwright install
RUN playwright install-deps

