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
