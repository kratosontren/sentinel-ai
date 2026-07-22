from kafka import KafkaConsumer
import json

from database.crud import save_post

consumer = KafkaConsumer(
    "news_topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode())
)

print("Waiting for messages...")

for message in consumer:

    post = message.value

    print(post["title"])

    save_post(post)