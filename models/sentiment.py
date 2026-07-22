from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)


def predict_sentiment(text):

    text = text[:512]

    result = classifier(text)[0]

    return {
        "label": result["label"],
        "score": float(result["score"])
    }