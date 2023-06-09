import streamlit as st
from kafka import KafkaConsumer

# Kafka consumer configuration
bootstrap_servers = '<confluent_cloud_bootstrap_servers>'
sasl_username = '<confluent_cloud_username>'
sasl_password = '<confluent_cloud_password>'
topic_name = 'processed-data'

# Set up Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password
)

# Set up Streamlit app
st.title('Network Traffic Analysis Dashboard')

# Read and display the processed data from Kafka topic
for message in consumer:
    window, source_ip, total_bytes_sent = message.value.decode('utf-8').split(',')
    st.write('Window:', window)
    st.write('Source IP:', source_ip)
    st.write('Total Bytes Sent:', total_bytes_sent)
    st.write('---')  # Add a separator between data points
