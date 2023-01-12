# Skill Assessment Task

## Pyspark Consumer

Project structure:


```
pyspark-consumer/
 |-- app/
 |   |-- application/ (ETL module used by main script)
 |   |-- | -- __init__.py  
 |   |-- | -- ingest.py  
 |   |-- | -- transform.py  
 |   |-- | -- persist.py 
 |   |-- configs/
 |   |-- | -- config.ini  (config file used for variables)
 |   |-- | -- ticker_schema.json  (schema to parse messages from kafka)
 |   |-- data_application.py ( main file)
 |-- jars/ (.jar dependencies needed to run pyspark code)
 |   Dockerfile 
 |   start-spark.sh (script to start any spark component, depending on env passed on the docker-compose file)
```

To create user image locally, standing on pyspark-consumer, run `docker build -t apache-spark:3.2.0`