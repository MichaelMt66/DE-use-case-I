FROM python:3.9-slim-buster

RUN apt update && apt install -y make && \
    useradd -d /app --create-home app && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /python-producer
COPY . /python-producer
WORKDIR /python-producer
RUN pip install -r requirements.txt
CMD ["python", "app/stocks_producer.py"]