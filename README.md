# Kafka Data Streaming
In this case study we take stored stock market data and transfer it over Apache Kafka's producer/consumer model to the client's S3 bucket where it is further used, e.g. for advertising purposes. This happens in real time.

## Architecture
![Kafka Architecture](https://i.ibb.co/R4DvKck/Kafka-drawio.png "Kafka Architecture")


### Kafka Broker
A Kafka cluster consists of one or more servers (Kafka brokers) running Kafka.

### Producer
Producers are processes that push records into Kafka topics within the broker.

### Consumer
A consumer pulls records off a Kafka topic.

### Kafka Connect
Kafka Connect makes it easy to stream from numerous sources into Kafka and from Kafka into numerous sources, with hundreds of available connectors. Kafka Connectors are available ready-made and can be programmed by oneself, as we do here.

### Database
The database contains stock market data.

### S3 Bucket
The data is transferred into client's S3 Bucket.

## Kafka Connect Producer API (Python)
```
pip install kafka-python
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json
producer = KafkaProducer(bootstrap_servers=['13.201.48.76:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
producer.send('<topic_name>' , value="{'i love kafka' : 'world'}")
```


