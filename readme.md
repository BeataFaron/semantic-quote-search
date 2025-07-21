# 🔍 Semantic Quote Search – Business Leaders & Innovators

This project is a **semantic search engine** that allows users to explore **inspirational business quotes** by meaning – not just by keywords.

> Built using `sentence-transformers`, `FAISS`, and `Streamlit`, the app demonstrates modern NLP capabilities on a curated quote dataset.

---

## 📌 Project Overview

- 💬 **Goal**: Enable users to search for relevant quotes by entering natural language queries (e.g. "failures in leadership", "long-term vision").
- 🔎 **Technique**: Uses sentence embeddings + cosine similarity (via FAISS) to match user queries with quote meanings.
- 💼 **Dataset**: 2,500+ quotes from real business leaders and innovators, enriched with metadata like theme, region, gender, decade, and more.

---

## 🧠 Key Features

- **Semantic Search** – powered by `all-MiniLM-L6-v2` model from `sentence-transformers`.
- **Metadata Filtering** – by theme (e.g. innovation, failure, teamwork).
- **Streamlit Web App** – for simple, user-friendly exploration.
- **Data Curation** – includes quotes from real sources (books, speeches, interviews), semi-manually scraped and enriched.

---

## 📂 Project Structure

semantic-quote-search/
│
├── data/
│ └── quotes-wisdom.csv # Final full dataset with metadata
│
├── notebooks/
│ ├── 01_scraping_quotes.ipynb # Scraping + cleaning quotes
│ └── 02_semantic_search_with_faiss.ipynb # Semantic search logic + app code
│
├── app.py # Streamlit application
├── requirements.txt # Required Python packages
├── README.md # This file
└── LICENSE


---

## 🚀 Demo: Streamlit App

🔗 [Launch the live app](https://semantic-quote-leadership-search.streamlit.app)

**How it works:**
1. Enter a **natural language query** (e.g., *"resilience in business"*).
2. The model returns quotes **similar in meaning**.
3. Filter results by **theme** (e.g., *Leadership*, *Innovation*).

---

## 📊 Dataset & Notebook on Kaggle

- 📁 [Kaggle Dataset: *Wisdom from Business Leaders & Innovators*](https://www.kaggle.com/datasets/beatafaron/wisdom-from-business-leaders-and-innovators)

- 📓 [Kaggle Notebook (Tutorial)](https://www.kaggle.com/code/beatafaron/semantic-search-tutorial-business-quote-finder)

---

## 🧰 Tech Stack

- `Python`
- `pandas`, `numpy`
- `sentence-transformers`
- `FAISS`
- `Streamlit`
- `Kaggle Datasets`

---

## 👩‍💻 Author

**Beata Faron** – Data Scientist (career transition from business + design).  
💼 [LinkedIn](https://www.linkedin.com/in/beata-faron-24764832)  
📊 [Kaggle](https://www.kaggle.com/beatafaron)  
📁 [GitHub Portfolio](https://github.com/BeataFaron)

---

## 📄 License

MIT License
