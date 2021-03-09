FROM python:3.8

WORKDIR /collabera

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY mac_get_manufacturer.py .