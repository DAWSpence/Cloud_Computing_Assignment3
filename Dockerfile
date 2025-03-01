FROM python:3.9-slim

WORKDIR /home/data
RUN mkdir /home/data/output
COPY script.py IF-1.txt AlwaysRememberUsThisWay-1.txt ./
COPY result.txt ./output

CMD [ "python3","script.py" ]

