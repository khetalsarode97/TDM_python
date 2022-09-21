# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR C:\ProgramData\Docker\Test_Data_Management

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]