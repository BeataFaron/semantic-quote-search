# Semantic Quote Search – Business Wisdom Finder 🔍

This project demonstrates a semantic search engine for inspirational quotes from business leaders and innovators. It uses `sentence-transformers` and `FAISS` to match user queries to meaningful quotes – going beyond simple keyword search.

---

## 📘 Dataset

All quotes and metadata come from a curated dataset available on Kaggle:  
📎 [Wisdom from Business Leaders and Innovators](https://www.kaggle.com/datasets/beatafaron/wisdom-from-business-leaders-and-innovators)

Includes:
- 2,500+ quotes (real)
- Metadata: theme, gender, region, decade, source, position

---

## 🧠 Project Structure

| File | Description |
|------|-------------|
| `01_scraping_quotes.ipynb` | Scrapes quotes from Wikiquote and enriches them with tags and metadata |
| `02_semantic_search_with_faiss.ipynb` | Generates embeddings, builds FAISS index, returns top semantic matches |
| `app.py` | Streamlit app for semantic search with filters |
| `quotes-wisdom.csv` | Cleaned dataset used by the app |
| `streamlit_app.md` | Link and description of the live demo |

---

## 🚀 Try the App

👉 [Live on Streamlit](https://semantic-quote-search.streamlit.app)

Type in a topic like _"innovation"_, _"failure"_ or _"growth"_ and get semantically matched quotes.

---

## 🧰 Tech Stack

`Python`, `Pandas`, `BeautifulSoup`, `SentenceTransformers`,  
`FAISS`, `Streamlit`, `scikit-learn`

---

## 👩‍💻 Author

Beata Faron  
- 💼 [LinkedIn](https://www.linkedin.com/in/beata-faron-24764832/)  
- 🧠 [Kaggle](https://www.kaggle.com/beatafaron)

---

⭐ If you like the project, feel free to star the repo or fork it!
