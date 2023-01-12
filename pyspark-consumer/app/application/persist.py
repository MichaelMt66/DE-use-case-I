import logging
import logging.config


class Persist:

    def __init__(self, spark):
        self.spark = spark

    def write_data(self, df):
        try:
            logger = logging.getLogger("Persist")
            logger.info('Persisting')

            df.writeStream \
                .format("console") \
                .outputMode("complete") \
                .option("truncate", "false") \
                .trigger(processingTime='30 seconds') \
                .start() \
                .awaitTermination()

        except Exception as exp:
            logger.error("An error occured while persisiting data >" + str(exp))
