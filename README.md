# Data Enginering - Use Case I

Create data pipeline that includes:

1. A data producer that generates and streams data to Kafka.
2. A data consumer that streams and aggregates data from Kafka.
3. Kafka to stream data between a consumer and a producer

The solution must be fully working using separate docker containers. A single docker-compose file should be created to run the entire pipeline.

Create a docker-compose file with all the containers. We should be able to run the full solution using the docker-compose tool. The docker-compose should have all the needed containers:

1. Kafka publisher container: should send a continuous stream of stock ticker data into Kafka topic named “stocks” (10 msgs per sec).

    * Data to send are in JSON format

    ```
    { "tickers": [{ "name": "AMZN", "price": 1902 },{
    "name": "MSFT", "price": 107 },{ "name": "AAPL", "price": 215 } ] }
    ```

    * Each message should contain 1-3 stocks, price is integer (generate random

    * integer prices using above provided prices as mean prices with a +/- 10% values)

2. Kafka container (and Zookeeper): (use publicly available images from Docker Hub).

3. Kafka consumer container: This container should read from the Kafka topic “stocks”, aggregate the price ticker, every 30 sec, and print the average price per stock to console with a timestamp.

4. Other containers if needed E.g., Zookeeper, Flink, Spark etc. containers.


## Solution


All you need is to run the docker-compose file using `docker-compose up -d`, it automatically run 
the images, following the next strucure:

1. zookeeper - confluent opensource image 
2. kafka - confluente opensource image
3. python-producer - python script to produce records as the task asked.
4. spark-master - spark standalone master node.
5. spark-worker - spark standalone worker node.
6. spark-driver - container used to connect to the spark standalone cluster and execute pyspark application.

To get spark-driver ouput, run `docker logs spark-driver -f`.

> Consumer and producer information is in README.md inside pyspark-consumer and python-producer folders

> There's no need to create the images locally, docker-compose is taking images of my dockerhub personal repository

> It was tested using docker desktop for Mac ver 3.3.3 and resources needed were 2.6 GHz 6-Core Intel Core i7 and 16 GB


> Inside the folders there are more docs about the code.
