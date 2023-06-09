from kafka import KafkaProducer
import time
import random

# Kafka producer configuration
bootstrap_servers = '<confluent_cloud_bootstrap_servers>'
sasl_username = '<confluent_cloud_username>'
sasl_password = '<confluent_cloud_password>'
topic_name = 'network-traffic'

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password
)

# Generate and publish network traffic data to Kafka topic
while True:
    # Generate random network traffic data
    source_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    destination_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    bytes_sent = random.randint(1000, 100000)

    # Publish network traffic data to Kafka topic
    producer.send(topic_name, f"{source_ip},{destination_ip},{bytes_sent}".encode('utf-8'))

    # Wait for 1 second before generating the next network traffic data
    time.sleep(1)
