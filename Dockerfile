FROM python:3.9

LABEL maintainer='DAWIT AKALU'

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "main.py"]