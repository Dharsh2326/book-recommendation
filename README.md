# 📚 Mood-Based Book Recommender

A simple Flask-based web application that recommends books based on your mood using the Goodreads dataset. This project explores the idea of text-to-text mapping (mood ➝ book title) and works entirely offline, without any external APIs.

---

## 🌟 Features

- ✅ Mood-based book recommendation
- ✅ Clean, user-friendly interface
- ✅ Uses Goodreads tags to map moods
- ✅ No external API usage – fully local
- ✅ Extendable to foundation models (T5, BERT)

---

## 🧠 How It Works

1. User enters a mood (e.g., *happy*, *sad*, *romantic*)
2. The system looks for tags in the dataset that match the mood
3. Matches those tags to books using tag-book mapping
4. Recommends one of the top related books

---

## 📂 Dataset Used

- **books.csv** – Basic book metadata
- **book_tags.csv** – Links books to tags using tag IDs
- **tags.csv** – List of available tags

> Dataset Source: [Goodreads Books Dataset on Kaggle](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k)

---

## 🛠️ Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Backend       | Python, Flask     |
| Frontend      | HTML, CSS         |
| Data Handling | Pandas            |
| Dataset       | Goodreads Dataset |

---
