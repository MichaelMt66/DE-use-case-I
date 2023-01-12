import logging
import logging.config
import configparser
from os import path


class Ingest:

    def __init__(self, spark):
        self.spark = spark

    def read_from_kafka(self):
        config = configparser.ConfigParser()
        config.read('configs/config.ini')
        bootstrap_servers = config.get('KAFKA_CONFIGS', 'KAFKA_BROKERS')
        topic = config.get('KAFKA_CONFIGS', 'KAFKA_TOPIC')

        df_raw = self.spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", bootstrap_servers) \
            .option("subscribe", topic) \
            .option("startingOffsets", "earliest") \
            .load()

        return df_raw