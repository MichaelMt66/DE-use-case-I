import sys
import logging
import logging.config
from application import ingest, transform, persist
from pyspark.sql import SparkSession


class Application:
    def run(self):
        try:
            logging.info('run_pipeline method started')
            ingest_process = ingest.Ingest(self.spark)
            df = ingest_process.read_from_kafka()
            # df.printSchema
            tranform_process = transform.Transform(self.spark)
            transformed_df = tranform_process.transform_data(df)
            persist_process = persist.Persist(self.spark)
            persist_process.write_data(transformed_df)
            logging.info('run_pipeline method ended')
        except Exception as exp:
            logging.error("An error occured while running the pipeline > " + str(exp))
            sys.exit(1)
            self.spark.stop()
        return

    def create_spark_session(self):
        self.spark = SparkSession \
            .builder \
            .appName("spark-kafka-stocs") \
            .getOrCreate()
            
        self.spark.sparkContext.setLogLevel("WARN")



if __name__ == '__main__':
    logging.info('Application started')
    app = Application()
    app.create_spark_session()
    logging.info('Spark Session created')
    app.run()
    logging.info('Process executed')