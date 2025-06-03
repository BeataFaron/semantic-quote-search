# 🔍 Semantic Quote Search

A web-based semantic search app built with **Streamlit**, **FAISS**, and **Sentence Transformers**. Users can enter natural language queries and retrieve the most relevant business quotes by meaning, not just keywords.

---

## 🚀 Demo

**Coming Soon:** [Live App on Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Project Structure

```
semantic-quote-search/
├── app.py                      # Streamlit app code
├── quotes_sample_500_cleaned.csv  # Dataset of business quotes
├── requirements.txt           # Dependencies
├── README.md                  # Project overview (this file)
```

---

## 📚 Features

* 🔍 Semantic search powered by sentence embeddings
* ⚡ Fast vector similarity using FAISS
* 🎨 Clean UI built with Streamlit
* 🧠 Contextual understanding, not just keyword matching
* 🧰 Optional filters by theme or metadata (if present)

---

## 🧠 Tech Stack

| Tool/Library          | Purpose                             |
| --------------------- | ----------------------------------- |
| Streamlit             | UI / App interface                  |
| Sentence Transformers | Embedding generation (MiniLM model) |
| FAISS                 | Fast vector indexing + similarity   |
| Pandas                | Data handling                       |
| NumPy                 | Vector math                         |

---

## 💡 How It Works

1. Quotes are embedded into high-dimensional vectors.
2. User query is also embedded and normalized.
3. FAISS finds the most similar vectors using cosine similarity.
4. Results are shown in ranked order with optional filters.

---

## 📦 Installation & Run Locally

```bash
# Clone repo and install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## ✍️ Author

Created by Beata Faron. Built for learning, portfolio, and AI/NLP practice.

---

## 📜 License

This project is open-source and licensed under the MIT License.

---

## 🌟 Future Improvements

* Add support for full dataset (2,500 quotes)
* Support filtering by author/gender/region
* Host on Hugging Face or Streamlit Cloud
* Add re-ranking using cross-encoders
