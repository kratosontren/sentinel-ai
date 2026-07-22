import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="SENTINEL",
    page_icon="◈",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

st_autorefresh(interval=30000, key="refresh")

# ======================================================
# CSS
# ======================================================

st.markdown("""
<style>

.stApp{
    background:#080B12;
}

.block-container{
    max-width:1500px;
    padding-top:1rem;
}

#MainMenu, footer, header{
    visibility:hidden;
}

.hero{
    background:
    linear-gradient(
        135deg,
        #08111E,
        #091423,
        #0A1628
    );

    border-radius:32px;

    padding:35px 45px;

    border:1px solid rgba(255,255,255,.08);

    box-shadow:
        0 20px 60px rgba(0,0,0,.45);
}

.metric-box{
    background:#0F141C;

    padding:25px;

    border-radius:24px;

    border:1px solid rgba(255,255,255,.06);

    box-shadow:
        0 10px 35px rgba(0,0,0,.35);
}

.section-title{
    color:#7B8794;
    font-size:13px;
    letter-spacing:2px;
    margin-top:25px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# DATA
# ======================================================

try:

    posts = requests.get(
        f"{API_URL}/posts",
        timeout=5
    ).json()

    sentiment = requests.get(
        f"{API_URL}/sentiment-distribution",
        timeout=5
    ).json()

    topics = requests.get(
        f"{API_URL}/topic-distribution",
        timeout=5
    ).json()

except:

    st.error("Backend is not running.")
    st.stop()

df = pd.DataFrame(posts)

# ======================================================
# HEADER
# ======================================================

st.markdown(f"""
<div class='hero'>

<h1 style='
font-size:64px;
font-weight:700;
letter-spacing:4px;
margin-bottom:20px;
'>

SENTI<span style='color:#3B82F6'>
NEL
</span>

</h1>

<div style='
font-size:22px;
color:#8B97A8;
margin-bottom:40px;
'>

Real-Time Sentiment Intelligence Platform

</div>

<div style='font-size:18px;'>

🟢 API ONLINE
&nbsp;&nbsp;&nbsp;
⚡ KAFKA ACTIVE
&nbsp;&nbsp;&nbsp;
🤖 ROBERTA RUNNING

</div>

<br>

<div style='
font-size:16px;
color:#7B8794;
'>

Last Refresh:
{datetime.now().strftime("%H:%M:%S")}

</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# KPI
# ======================================================

positive = sentiment.get("positive", 0)
neutral = sentiment.get("neutral", 0)
negative = sentiment.get("negative", 0)

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.metric(
            "📰 Articles",
            len(df)
        )

with c2:
    with st.container(border=True):
        st.metric(
            "😊 Positive",
            positive
        )

with c3:
    with st.container(border=True):
        st.metric(
            "😐 Neutral",
            neutral
        )

with c4:
    with st.container(border=True):
        st.metric(
            "☹️ Negative",
            negative
        )

# ======================================================
# CHARTS
# ======================================================

st.markdown(
    "<div class='section-title'>ANALYTICS</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    if sentiment:

        sdf = pd.DataFrame(
            list(sentiment.items()),
            columns=[
                "Sentiment",
                "Count"
            ]
        )

        fig = px.pie(
            sdf,
            names="Sentiment",
            values="Count",
            hole=.7
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    if topics:

        tdf = pd.DataFrame(
            list(topics.items()),
            columns=[
                "Topic",
                "Count"
            ]
        )

        tdf = tdf.sort_values(
            "Count",
            ascending=False
        )

        fig = px.bar(
            tdf,
            x="Count",
            y="Topic",
            orientation="h"
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ======================================================
# CONFIDENCE
# ======================================================

if (
    "confidence" in df.columns
    and not df["confidence"]
    .dropna()
    .empty
):

    st.markdown(
        "<div class='section-title'>MODEL CONFIDENCE</div>",
        unsafe_allow_html=True
    )

    fig = px.histogram(
        df,
        x="confidence",
        nbins=20
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=350
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# SEARCH
# ======================================================

st.markdown(
    "<div class='section-title'>ARTICLE EXPLORER</div>",
    unsafe_allow_html=True
)

search = st.text_input(
    "Search Articles"
)

filtered = df.copy()

if search and "title" in filtered.columns:

    filtered = filtered[
        filtered["title"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ======================================================
# ARTICLES
# ======================================================

for _, row in filtered.head(15).iterrows():

    with st.container(border=True):

        st.markdown(
            f"### {row.get('title','Untitled')}"
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.write(
                f"Topic: {row.get('topic','N/A')}"
            )

        with c2:
            st.write(
                f"Sentiment: {row.get('sentiment','N/A')}"
            )

        with c3:
            st.write(
                f"Confidence: {round(row.get('confidence',0),3)}"
            )

        if row.get("url"):
            st.link_button(
                "Read Article",
                row["url"]
            )

# ======================================================
# EXPORT
# ======================================================

st.download_button(
    "📥 Download CSV",
    filtered.to_csv(index=False),
    file_name="sentiment_data.csv",
    mime="text/csv"
)