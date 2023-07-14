FROM ubuntu:18.04
LABEL title="node-exporter"
LABEL maintainer="parkgyeongtae"

# apt 미러서버 미국(default) -> 한국 변경
RUN sed -i 's@archive.ubuntu.com@kr.archive.ubuntu.com@g' /etc/apt/sources.list

# 자주 사용하는 패키지 설치
RUN apt-get update && \
    apt-get install wget -y

# 작업 영역
WORKDIR /home

# node exporter 1.3.1
RUN wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz && \
    tar -zxf node_exporter-1.3.1.linux-amd64.tar.gz && \
    mv node_exporter-1.3.1.linux-amd64 node_exporter && \
    rm -rf node_exporter-1.3.1.linux-amd64.tar.gz

ENTRYPOINT /home/node_exporter/node_exporter --web.listen-address=:9500 & bash