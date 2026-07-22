import json
from kafka import KafkaProducer
from pathlib import Path


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:
        json.dumps(v).encode("utf-8")
)


BASE_DIR = Path(__file__).resolve().parents[1]

file_path = (
    BASE_DIR
    / "data"
    / "raw"
    / "news_posts.json"
)


with open(
    file_path,
    "r",
    encoding="utf-8"
) as f:

    posts = json.load(f)


for post in posts:

    producer.send(
        "news_topic",
        value=post
    )

    print(
        f"Sent -> {post['title'][:60]}"
    )


producer.flush()

print(
    "\nFinished sending messages."
)