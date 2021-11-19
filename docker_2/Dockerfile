FROM prefecthq/prefect:latest

RUN apt-get update
RUN apt-get install -y telnet

RUN pip install --upgrade pip

COPY config.toml /root/.prefect

#WORKDIR /app

COPY . .
RUN pip install .
