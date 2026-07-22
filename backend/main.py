from fastapi import FastAPI
from database.db import SessionLocal
from database.models import NewsPost

app = FastAPI()


@app.get("/")
def root():

    return {
        "message": "API Running Successfully"
    }


@app.get("/posts")
def get_posts():

    db = SessionLocal()

    try:

        posts = db.query(NewsPost).all()

        result = []

        for p in posts:

            result.append({
                "id": p.id,
                "title": p.title,
                "text": p.text,
                "topic": p.topic,
                "source": p.source,
                "url": p.url,
                "sentiment": p.sentiment,
                "confidence":
                    float(p.confidence)
                    if p.confidence is not None
                    else None,

                "processed_at":
                    str(p.processed_at)
                    if p.processed_at
                    else None
            })

        return result

    except Exception as e:

        return {
            "error": str(e)
        }

    finally:
        db.close()

    return result


@app.get("/posts/{post_id}")
def get_post(post_id: int):

    db = SessionLocal()

    p = (
        db.query(NewsPost)
        .filter(
            NewsPost.id == post_id
        )
        .first()
    )

    db.close()

    if not p:

        return {
            "error": "Post not found"
        }

    return {

        "id": p.id,
        "title": p.title,
        "text": p.text,
        "topic": p.topic,
        "source": p.source,
        "url": p.url,
        "sentiment": p.sentiment,

        "confidence":
            float(p.confidence)
            if p.confidence is not None
            else None,

        "processed_at":
            p.processed_at.isoformat()
            if p.processed_at
            else None
    }


@app.get("/latest")
def latest():

    db = SessionLocal()

    posts = (

        db.query(
            NewsPost
        )

        .order_by(
            NewsPost.id.desc()
        )

        .limit(20)

        .all()
    )

    result = []

    for p in posts:

        result.append({

            "id": p.id,
            "title": p.title,
            "topic": p.topic,
            "sentiment": p.sentiment,

            "confidence":
                float(p.confidence)
                if p.confidence is not None
                else None
        })

    db.close()

    return result


@app.get("/sentiment-distribution")
def sentiment_distribution():

    db = SessionLocal()

    posts = db.query(
        NewsPost
    ).all()

    data = {}

    for p in posts:

        if p.sentiment:

            data[p.sentiment] = (

                data.get(
                    p.sentiment,
                    0
                ) + 1
            )

    db.close()

    return data


@app.get("/topic-distribution")
def topic_distribution():

    db = SessionLocal()

    posts = db.query(
        NewsPost
    ).all()

    data = {}

    for p in posts:

        if p.topic:

            data[p.topic] = (

                data.get(
                    p.topic,
                    0
                ) + 1
            )

    db.close()

    return data