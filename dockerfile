FROM python:3.12


RUN apt-get update -yy
#RUN apt-get upgrade -yy
RUN apt install -yy \
    g++ gcc libxml2-dev \
    libxslt-dev libffi-dev \
    make curl

COPY . /home/ransomwatch
RUN mkdir /home/ransomwatch/source 
RUN touch /home/ransomwatch/posts.json
RUN echo "[  ]" >> /home/ransomwatch/posts.json

# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r /home/ransomwatch/requirements.txt

RUN playwright install
RUN playwright install-deps

