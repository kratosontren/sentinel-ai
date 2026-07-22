from datetime import datetime

from database.db import SessionLocal
from database.models import NewsPost
from models.sentiment import predict_sentiment


db = SessionLocal()

posts = (
    db.query(NewsPost)
      .filter(NewsPost.sentiment == None)
      .all()
)

print(f"Found {len(posts)} posts")


for i, post in enumerate(posts, start=1):

    text = f"{post.title} {post.text}"

    try:

        result = predict_sentiment(text)

        post.sentiment = result["label"]
        post.confidence = result["score"]
        post.processed_at = datetime.utcnow()

        print(
            f"[{i}/{len(posts)}]",
            result["label"],
            round(result["score"], 3),
            post.title[:60]
        )

    except Exception as e:

        print(f"Error processing post {i}: {e}")

db.commit()
db.close()

print("Sentiment analysis completed.")