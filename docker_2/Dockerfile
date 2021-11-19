FROM prefecthq/prefect:latest

RUN apt-get update
RUN apt-get install -y telnet

COPY config.toml /root/.prefect

WORKDIR /app

COPY docker_2.py .
