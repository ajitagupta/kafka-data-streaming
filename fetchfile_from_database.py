from confluent_kafka import Producer
import psycopg2
import json

# Kafka broker configurations
bootstrap_servers = 'localhost:9092'
topic = 'your_topic'

# Database configurations
db_host = 'your_db_host'
db_name = 'your_db_name'
db_user = 'your_db_user'
db_password = 'your_db_password'

# Create a Kafka producer
producer = Producer({'bootstrap.servers': bootstrap_servers})

# Function to fetch data from the database
def fetch_data():
    conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to send data to Kafka broker
def send_to_kafka(data):
    for row in data:
        # Assuming each row is a dictionary
        # Convert row to JSON format
        message = json.dumps(row)
        # Send message to Kafka topic
        producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()

# Delivery report callback function
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to topic {msg.topic()}")

if __name__ == '__main__':
    # Fetch data from database
    data = fetch_data()
    # Send data to Kafka broker
    send_to_kafka(data)
-----------------------------------
### Note-1----Make sure to replace 'your_topic', 'your_db_host', 'your_db_name', 'your_db_user', 'your_db_password', and 'your_table' with your actual Kafka topic, database host, database name, database username, database password, and table name respectively.
### Note-2----Also, ensure that you have installed psycopg2 for interacting with PostgreSQL database and confluent_kafka for interacting with Kafka broker. You can install them via pip:
### pip install psycopg2 confluent_kafka
