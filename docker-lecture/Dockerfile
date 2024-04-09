FROM python:3.11-bullseye

RUN pip install pandas

COPY iris.csv /tmp/iris.csv

COPY iris.py /tmp/iris.py

WORKDIR /tmp

CMD sleep 1000
#CMD python iris.py