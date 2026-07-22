from database.db import SessionLocal
from database.models import NewsPost


def save_post(post):

    db = SessionLocal()

    existing = (
        db.query(NewsPost)
        .filter(
            NewsPost.url ==
            post["url"]
        )
        .first()
    )

    if existing:

        db.close()
        return

    news = NewsPost(

        title=post["title"],
        text=post["text"],
        topic=post["topic"],
        source=post["source"],
        url=post["url"]
    )

    db.add(news)

    db.commit()

    db.close()