import os

folders = [
    "ingestion/reddit",
    "ingestion/twitter",
    "ingestion/utils",
    "processing",
    "models",
    "backend",
    "dashboard",
    "database",
    "docker",
    "data/raw",
    "data/processed",
    "configs",
    "docs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

files = [
    ".env",
    "README.md",
    "ingestion/reddit/client.py",
    "ingestion/reddit/fetch.py",
    "ingestion/twitter/login.py",
    "ingestion/twitter/fetch.py",
    "ingestion/utils/normalizer.py"
]

for file in files:
    open(file, "a").close()

print("Project Structure Created Successfully!")