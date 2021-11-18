FROM prefecthq/prefect:latest

RUN apt-get update
RUN apt-get install -y telnet

WORKDIR /app

COPY hello_docker_2.py .
