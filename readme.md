# Semantic Quote Search – Business Wisdom Finder 🧠🔍

This project enables semantic search over quotes from business leaders and innovators. It combines scraping, metadata tagging, sentence embeddings, and FAISS indexing to allow fast, meaningful quote retrieval based on user queries.

---

## 📘 Dataset

The data is public and available on Kaggle:  
👉 [Wisdom from Business Leaders and Innovators](https://www.kaggle.com/datasets/beatafaron/wisdom-from-business-leaders-and-innovators)

It includes:
- 2,500+ real quotes
- Metadata: tags (themes), decade, gender, region, occupation
- Cleaned and deduplicated content

---

## 🧪 Project Structure

| Notebook | Description |
|----------|-------------|
| **01** – Scraping Quotes | Quote scraping (Wikiquote), tag extraction, cleaning |
| **02** – Semantic Search with FAISS | Sentence embedding, FAISS index creation, top-k search |
| **03** – Final Demo (Kaggle) | Interactive demo with metadata filters and query examples |

---

## 🚀 What It Does

- Embeds quotes using `sentence-transformers` (MiniLM)
- Indexes embeddings with `FAISS` for ultra-fast retrieval
- Supports filtering by metadata (e.g., only female innovators in the 1980s)
- Matches user queries based on meaning (not keywords)

---

## 🧰 Tech Stack

`Python`, `Pandas`, `BeautifulSoup`, `SentenceTransformers`,  
`FAISS`, `scikit-learn`, `Matplotlib`, `Streamlit` (planned)

---

## 📂 Related Links

- 📊 [Kaggle Dataset](https://www.kaggle.com/datasets/beatafaron/wisdom-from-business-leaders-and-innovators)  
- 📘 [Kaggle Notebook – Semantic Quote Search](https://www.kaggle.com/code/beatafaron/semantic-search-tutorial-business-quote-finder)

---

## 👩‍💻 Author

Beata Faron  
- 💼 [LinkedIn](https://www.linkedin.com/in/beata-faron-24764832/)  
- 🧠 [Kaggle](https://www.kaggle.com/beatafaron)

---

⭐ If you found this useful, feel free to star the repo and connect!
