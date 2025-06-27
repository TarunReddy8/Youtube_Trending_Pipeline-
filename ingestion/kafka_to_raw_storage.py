# File: ingestion/kafka_to_raw_storage.py
from kafka import KafkaConsumer
import json
import os
from datetime import datetime

KAFKA_TOPIC = "yt_trending"
KAFKA_SERVER = "localhost:9092"
RAW_DIR = "data/raw"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def store_raw_data(record):
    date_str = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
    file_path = os.path.join(RAW_DIR, f"video_{record['id']}_{date_str}.json")
    with open(file_path, 'w') as f:
        json.dump(record, f, indent=2)
    print(f"Saved: {file_path}")

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    print("Listening to Kafka...")
    for message in consumer:
        store_raw_data(message.value)

if __name__ == "__main__":
    main()