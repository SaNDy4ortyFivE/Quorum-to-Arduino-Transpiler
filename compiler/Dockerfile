FROM ubuntu:latest

RUN apt-get -y update && apt-get -y upgrade
RUN apt install -y default-jre
RUN apt install -y default-jdk
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install tornado
RUN pip3 install pyrebase

RUN mkdir q_compiler

COPY source_files/ q_compiler/

WORKDIR q_compiler/quorum_runner

CMD ["python3", "server.py"]
