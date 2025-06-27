
# File: ingestion/youtube_kafka_producer.py
import requests
import json
import time
from kafka import KafkaProducer

API_KEY = "AIzaSyCD72zGUCQ8iXmnf7sptqci1ByN5xYrDcM"
KAFKA_TOPIC = "yt_trending"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_trending_videos(region_code="US"):
    url = (
        f"https://www.googleapis.com/youtube/v3/videos?"
        f"part=snippet,contentDetails,statistics&chart=mostPopular&regionCode={region_code}"
        f"&maxResults=10&key={API_KEY}"
    )
    print("Requesting URL:", url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Failed to fetch: {response.status_code}")
        return []

def send_to_kafka(videos):
    for video in videos:
        producer.send(KAFKA_TOPIC, video)
        print(f"Sent to Kafka: {video['id']}")

def main():
    while True:
        videos = fetch_trending_videos()
        send_to_kafka(videos)
        print("Sleeping for 10 minutes...")
        time.sleep(600)

if __name__ == "__main__":
    main()
