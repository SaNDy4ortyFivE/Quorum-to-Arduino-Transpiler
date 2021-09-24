FROM ubuntu:latest

RUN apt-get -y update && apt-get -y upgrade
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install tornado
RUN pip3 install antlr4-python3-runtime
RUN pip3 install anytree
RUN pip3 install pyrebase

RUN mkdir myapp

COPY source_files/ myapp/

WORKDIR myapp

RUN mkdir quorum_user_code

CMD ["python3", "server.py"]
