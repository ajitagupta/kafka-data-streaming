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
Kafka Connect makes it easy to stream from numerous sources into Kafka and from Kafka into numerous sources, with hundreds of available connectors. Kafka connectors are available ready-made but can also be written by oneself, as we do here.

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
producer = KafkaProducer(bootstrap_servers=['<publicIP>:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
df = pd.read_csv("indexProcessed.csv")
df.head()
df.sample(1)
while True:
  dict_stock = df.sample(1).to_dict(orient="records")[0]
  producer.send('<tpoic_name>', value=dict_stock)
  sleep(1)
producer.flush()
```

## Kafka Connect Consumer API (Python)
```
from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem
consumer = KafkaConsumer(
    '<topic_name>',
     bootstrap_servers=['<publicIP>:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))
for c in consumer:
     print(c.value)
s3 = S3FileSystem()
for count, i in enumerate(consumer):
    with s3.open("s3://<your_bucket_name>/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file) 

----------------------------------------------------------

Prequisites:
1-- AWS CLI username/password
2-- Access for s3 bucket
```

