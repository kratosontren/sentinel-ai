import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from apscheduler.schedulers.blocking import BlockingScheduler
from ingestion.rss.fetch import fetch_news


scheduler = BlockingScheduler()

scheduler.add_job(
    fetch_news,
    trigger="interval",
    hours=1
)

print("Scheduler Running...")

scheduler.start()