import logging
import logging.config
from application import ingest, transform
from pyspark.sql.types import *
from pyspark.sql.functions import from_json, col, explode, current_timestamp, avg
import json


class Transform:

    def __init__(self, spark):
        self.spark = spark

        
    def get_schema(self):
        with open('configs/ticker_schema.json', 'r') as F:
            ticker_schema = json.load(F)

        ticker_schema_json = json.dumps(ticker_schema)
        schema = StructType.fromJson(json.loads(ticker_schema_json))
        return schema
    
        
    def transform_data(self, df):
        logger = logging.getLogger("Transform")
        logger.info("Transforming")
        logger.warning("Warning in Transformer")

        schema = self.get_schema()

        parsed_df = df \
            .select(from_json(col("value").cast("string"), schema).alias("parsed_value")) \
            .select("parsed_value.tickers")

        final = parsed_df \
            .select(explode("tickers").alias("ticker")) \
            .select("ticker.name", "ticker.price") \
            .groupBy("name").agg(avg("price").alias("average_stock_price")) \
            .withColumn("current_timestamp", current_timestamp())

        return final

