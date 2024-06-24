# docker build --network host -t ran .
FROM debian:12

RUN apt-get update -y
#RUN apt-get upgrade -yy
RUN apt-get install -y \
    g++ gcc libxml2-dev \
    libxslt-dev libffi-dev \
    make curl python3 pip \
    vim

COPY . /home/ransomwatch

RUN pip3 install -r /home/ransomwatch/requirements.txt \
--break-system-packages

RUN playwright install
RUN playwright install-deps