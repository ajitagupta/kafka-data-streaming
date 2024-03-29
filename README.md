# Kafka Data Streaming
In this case study we take stored shoe data and transfer it over Apache Kafka's producer/consumer model to the client's S3 bucket.

## Architecture
![Kafka Architecture](https://i.ibb.co/R4DvKck/Kafka-drawio.png "Kafka Architecture")


### Kafka Broker
A Kafka cluster consists of one or more servers (Kafka brokers) running Kafka.

### Producer
Producers are processes that push records into Kafka topics within the broker.

### Consumer
A consumer pulls records off a Kafka topic.

### Kafka Connect
Kafka Connect makes it easy to stream from numerous sources into Kafka and from Kafka into numerous sources, with hundreds of available connectors.

### Database
The database contains sports data.

### S3 Bucket
The data is transferred into client's S3 Bucket.



