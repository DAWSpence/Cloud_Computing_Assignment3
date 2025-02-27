FROM ubuntu

WORKDIR /home/data
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .
COPY result.txt ./output
RUN mkdir /home/data/output

RUN apt update \
	&& apt install python3


