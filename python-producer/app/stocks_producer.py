from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from random import randint
import json
import random
import schedule
import configparser
import logging
import logging.config


def main(bootstrap_servers, topic):
    producer_conf = {'bootstrap.servers': bootstrap_servers,
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': StringSerializer('utf_8')}

    producer = SerializingProducer(producer_conf)

    schedule.every(1).second.do(send_data_to_kafka, producer, topic)
    while True:
        schedule.run_pending()


def random_json_producer():
    data = [
        {"name": "AMZN", "price": 1902},
        {"name": "MSFT", "price": 107},
        {"name": "AAPL", "price": 215}
    ]

    stocks_variance = [0.9, 1.1]

    # Applying variances to stocks prices
    data[0]['price'] = int(data[0]['price'] * random.choice(stocks_variance))
    data[1]['price'] = int(data[1]['price'] * random.choice(stocks_variance))
    data[2]['price'] = int(data[2]['price'] * random.choice(stocks_variance))

    # Shuffling and take first 1-3 values
    random.shuffle(data)
    stocks = data[:randint(1, 3)]
    tickers = json.dumps({'tickers': stocks})

    return tickers


def send_data_to_kafka(producer, topic):

    logging.info('generating following records and sending them')

    for i in range(10):
        producer.poll(0.0)
        try:
            tickers = random_json_producer()
            logging.info(tickers)
            producer.produce(topic=topic, key=None, value=tickers, on_delivery=delivery_report)
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Invalid input, discarding record...")
            continue

    logging.info("Flushing records...")
    producer.flush()


def delivery_report(err, msg):
    if err is not None:
        logging.error("Delivery failed for record {}: {}".format(msg.key(), err))
        return
    logging.info('Records {} successfully produced to {} [{}] at offset {}'.format(
        msg.value(), msg.topic(), msg.partition(), msg.offset()))


if __name__ == '__main__':
    # Getting configs
    config = configparser.ConfigParser()
    config.read('/python-producer/app/resources/config.ini')
    logging.config.fileConfig("/python-producer/app/resources/logging.conf")

    # Settings values
    logging.info('run_pipeline method started')
    kafka_brokers = config.get('KAFKA_CONFIGS', 'KAFKA_BROKERS')
    kafka_topic = config.get('KAFKA_CONFIGS', 'KAFKA_TOPIC')
    main(kafka_brokers, kafka_topic)
