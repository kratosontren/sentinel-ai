import feedparser
import json
from ingestion.utils.clean_text import clean_text

feeds = {

    "technology":
    "https://feeds.feedburner.com/TechCrunch",

    "technology2":
    "https://www.theverge.com/rss/index.xml",

    "technology3":
    "https://feeds.arstechnica.com/arstechnica/index",

    "ai":
    "https://www.artificialintelligence-news.com/feed/",

    "ai2":
    "https://venturebeat.com/feed/",

    "world":
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",

    "world2":
    "http://feeds.bbci.co.uk/news/world/rss.xml",

    "world3":
    "https://www.aljazeera.com/xml/rss/all.xml"
}


def fetch_news():

    all_posts = []
    seen_urls = set()

    for topic, url in feeds.items():

        print(f"Fetching {topic}")

        feed = feedparser.parse(url)

        for entry in feed.entries:

            try:

                link = entry.get("link", "")

                if link in seen_urls:
                    continue

                seen_urls.add(link)

                title = entry.get("title", "")

                text = ""

                if "summary" in entry:
                    text = entry.summary

                text = clean_text(text)

                post = {
                    "title": title,
                    "text": text,
                    "topic": topic,
                    "source": feed.feed.get(
                        "title",
                        "Unknown"
                    ),
                    "url": link
                }

                all_posts.append(post)

            except Exception as e:
                print(e)

    print(f"Saved {len(all_posts)} posts")

    with open(
            "data/raw/news_posts.json",
            "w",
            encoding="utf-8"
    ) as f:

        json.dump(
            all_posts,
            f,
            indent=4,
            ensure_ascii=False
        )

    return all_posts


if __name__ == "__main__":
    fetch_news()