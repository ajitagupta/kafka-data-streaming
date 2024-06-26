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

# Prequisites:
### 1-- AWS CLI username/password
### 2-- Access for s3 bucket
