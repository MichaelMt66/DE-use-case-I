# Skill Assessment Task

## Python producer

Project structure:


```
python-producer/
 |-- app/
 |   |-- resources/
 |   |-- | -- config.ini  (config file used for variables)
 |   |-- | -- logging.conf  (logging config file)
 |   |-- stock-producer.py (script with the logic)
 |   Dockerfile
 |   requirements.txt (dependency libraries)
```

To create user image locally, standing on python-producer, run `docker build -t python-producer:1.0.0`

