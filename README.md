# ◈ SENTINEL
### Real-Time Sentiment Intelligence Platform

SENTINEL is an end-to-end real-time analytics platform that ingests live news streams, processes them through distributed data pipelines, performs sentiment analysis using transformer-based NLP models, and visualizes insights through an interactive monitoring dashboard.

---

## 🚀 Features

- Real-time RSS news ingestion
- Kafka-based streaming architecture
- PostgreSQL data persistence
- Transformer-based sentiment classification
- REST APIs using FastAPI
- Interactive Streamlit analytics dashboard
- Topic distribution analytics
- Model confidence monitoring
- Searchable article explorer
- CSV export functionality
- Dockerized deployment support

---

## 🏗️ System Architecture

```text
RSS Feeds
     ↓
Kafka Producer
     ↓
Kafka Consumer
     ↓
PostgreSQL Database
     ↓
RoBERTa Sentiment Model
     ↓
FastAPI Backend
     ↓
Streamlit Dashboard
```

---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

### Streaming & Data Engineering
- Apache Kafka
- Docker
- RSS Feed Processing

### Machine Learning / NLP
- HuggingFace Transformers
- RoBERTa
- PyTorch

### Frontend / Visualization
- Streamlit
- Plotly

### Languages & Tools
- Python
- Git
- GitHub

---

## 📊 Dashboard Features

### Executive Analytics Dashboard
- Total articles monitored
- Sentiment distribution tracking
- Topic volume analytics
- Model confidence monitoring
- Real-time system status indicators

### Article Intelligence Terminal
- Search articles by keywords
- Sentiment filtering
- External article linking
- CSV export support

---

## 📂 Project Structure

```text
sentinel-ai/

├── backend/
│   ├── routes/
│   └── schemas/
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── models.py
│   ├── crud.py
│   └── db.py
│
├── ingestion/
│   ├── reddit/
│   ├── twitter/
│   └── utils/
│
├── processing/
│   └── analyze_sentiment.py
│
├── streaming/
│   ├── producer.py
│   └── consumer.py
│
├── scheduler/
│
├── docker/
│
├── requirements.txt
├── README.md
└── docker-compose.yml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/kratosontren/sentinel-ai.git
cd sentinel-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐳 Start Infrastructure

```bash
docker compose up -d
```

Services Started:

- PostgreSQL
- Kafka
- Zookeeper

---

## ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## 📈 Run Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## 📡 API Endpoints

### Get Articles

```http
GET /posts
```

### Get Latest Articles

```http
GET /latest
```

### Sentiment Distribution

```http
GET /sentiment-distribution
```

### Topic Distribution

```http
GET /topic-distribution
```

---

## 🧠 Machine Learning Pipeline

1. News articles are ingested from RSS sources.
2. Articles are streamed through Kafka topics.
3. Data is persisted in PostgreSQL.
4. RoBERTa transformer performs sentiment inference.
5. Predictions are stored and served through APIs.
6. Dashboard visualizes analytics in real time.

---

## 📸 Dashboard Preview

### Main Dashboard

> Add screenshots here

```markdown
![Dashboard](docs/screenshots/dashboard.png)
```

---

## 🎯 Resume Highlights

- Built an end-to-end real-time analytics platform using Kafka, FastAPI, PostgreSQL, and Transformer models.
- Designed distributed data ingestion and processing pipelines for streaming news analytics.
- Developed interactive monitoring dashboards with real-time sentiment and topic intelligence.
- Integrated RoBERTa-based NLP models for automated sentiment classification.

---

## 🔮 Future Improvements

- Multi-language sentiment support
- Named Entity Recognition (NER)
- Trend forecasting
- User authentication
- Kubernetes deployment
- Vector database integration
- LLM-powered news summarization

---

## 👨‍💻 Author

**Gulam Mohd Khan**

B.Tech Artificial Intelligence  
Zakir Hussain College of Engineering & Technology, AMU

GitHub:
https://github.com/kratosontren
