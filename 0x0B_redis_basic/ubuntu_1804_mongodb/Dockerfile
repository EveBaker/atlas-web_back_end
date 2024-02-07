FROM docker.registry-private.hbtn.io/ubuntu_1804_python37

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list

RUN apt-get update

RUN mkdir -p /data/db

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles
RUN apt-get install -y tzdata

RUN apt-get install -y mongodb-org

RUN pip install --upgrade pip
RUN pip3 install pymongo

ADD init.d-mongod /etc/init.d/mongod
RUN chmod u+x /etc/init.d/mongod


