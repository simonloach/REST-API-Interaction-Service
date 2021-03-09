FROM python:3.8

WORKDIR /collabera

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY mac_get_manufacturer.py .

RUN echo '#! /bin/bash\npython /collabera/mac_get_manufacturer.py $@'>/bin/get_manufacturer

RUN chmod +x /bin/get_manufacturer
