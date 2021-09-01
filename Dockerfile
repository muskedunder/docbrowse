FROM python:3.8-slim as base

WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app ./app

##########################################
#####--- Create development image ---#####
##########################################

FROM base as dev

CMD bash -c 'uvicorn app.app:app --host 0.0.0.0'
