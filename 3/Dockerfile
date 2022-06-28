FROM python:3.11-rc

WORKDIR /app

RUN pip3 install colorama mysql-connector-python

COPY . .

ENTRYPOINT "/app/app-v3.py"
