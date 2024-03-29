# Kafka Data Streaming
In this case study we take stored shoe data and transfer it over Apache Kafka's producer/consumer model to the client's S3 bucket.

## Architecture


### Kafka Broker
A Kafka cluster consists of one or more servers (Kafka brokers) running Kafka.

### Producer
Producers are processes that push records into Kafka topics within the broker.

### Consumer
A consumer pulls records off a Kafka topic.

### Kafka Connect
Kafka Connect makes it easy to stream from numerous sources into Kafka and from Kafka into numerous sources, with hundreds of available connectors.
