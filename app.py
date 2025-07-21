import streamlit as st
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Semantic Quote Search", layout="centered")

# Load data and create FAISS index
@st.cache_data
def load_data():
    df = pd.read_csv("data/quotes-wisdom.csv")
    df = df.dropna(subset=["quote"]).reset_index(drop=True)
    df.rename(columns={"theme/tag": "theme"}, inplace=True)  # Normalize column name

    model = SentenceTransformer('all-MiniLM-L6-v2')
    quotes = df['quote'].tolist()
    embeddings = model.encode(quotes, convert_to_numpy=True)
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    return df, model, index, embeddings

df, model, index, embeddings = load_data()

# --- Optional: Debug info (you can remove later)
st.write("✅ Dataset preview:")
st.dataframe(df.head(3))

st.write("✅ Columns:")
st.write(df.columns.tolist())
# ---

# UI Layout
st.title("🔍 Semantic Quote Search")
st.write("Search through inspirational business quotes by meaning.")

# Sidebar filters
with st.sidebar:
    st.header("🔎 Filters")
    if 'theme' in df.columns:
        theme_filter = st.selectbox("Filter by theme:", ["All"] + sorted(df['theme'].dropna().unique().tolist()))
    else:
        st.warning("Column 'theme' not found. Filter disabled.")
        theme_filter = "All"

# Main input
query = st.text_input("Enter your question or topic:")

# Semantic Search
if query:
    q_vec = model.encode([query], convert_to_numpy=True)
    q_vec = q_vec / np.linalg.norm(q_vec, axis=1, keepdims=True)
    D, I = index.search(q_vec, k=10)

    st.subheader(f"Top Matches for: '{query}'")
    for idx, score in zip(I[0], D[0]):
        row = df.iloc[idx]
        if theme_filter != "All" and row.get("theme") != theme_filter:
            continue

        st.markdown(f"> *{row['quote']}*")
        st.caption(f"— {row['author']} ({row.get('theme', '')})")
        st.markdown(f"Similarity Score: `{score:.4f}`")
        st.markdown("---")

# About section
with st.expander("ℹ️ About this app"):
    st.write("""
        This app demonstrates a simple semantic search engine using FAISS and sentence-transformers.

        Enter any query, and it will return the most relevant business quotes based on meaning — not just keywords.

        Dataset: Curated business quotes for educational & portfolio use.
    """)
