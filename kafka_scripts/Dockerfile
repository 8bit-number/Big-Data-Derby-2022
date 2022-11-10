FROM python:3.9-alpine

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir kafka-python

CMD ["ls"]

# CMD ["python", "single_event_producer.py"]