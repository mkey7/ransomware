FROM python:3.12

RUN echo "https://mirrors.tuna.tsinghua.edu.cn/debian" > /etc/apt/mirrors/debian.list
RUN echo "https://mirrors.tuna.tsinghua.edu.cn/debian-security" > /etc/apt/mirrors/debian-security.list 

RUN apt-get update -yy
#RUN apt-get upgrade -yy
RUN apt install -yy \
    git

RUN pip3 install -r requirements.txt

RUN playwright install
RUN playwright install-deps


ENTRYPOINT ["python3", "ransomwatch.py"]