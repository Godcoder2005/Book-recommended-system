# 📚 Book Recommendation System

A content-based and collaborative filtering book recommendation system built with Python, trained on the [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/). Deployed as an interactive web app using Streamlit.

---

## 🚀 Live Demo

> Run locally using the instructions below.

---

## 🖼️ Screenshots

| Home Page (Top 50 Books) | Recommendation Page |
|:---:|:---:|
| Displays top 50 books by ratings | Enter a book and get 5 similar recommendations |

---

## 🧠 How It Works

### Collaborative Filtering Pipeline

```
Books.csv + Ratings.csv + Users.csv
        ↓
Filter: Books with 50+ ratings
Filter: Users who rated 200+ books
        ↓
Pivot Table → Book Title × User ID → Rating
        ↓
Cosine Similarity Matrix
        ↓
Top 5 Similar Books
```

1. **Data Filtering** — Only books with 50+ ratings and users who rated 200+ books are used to reduce noise and sparsity.
2. **Pivot Table** — A user-item matrix is created with book titles as rows and user IDs as columns, filled with ratings.
3. **Cosine Similarity** — Similarity between books is computed based on how similarly users rated them.
4. **Recommendation** — Given a book, the top 5 most similar books are returned based on cosine similarity scores.

---

## 🗂️ Project Structure

```
recommendation-system/
│
├── app.py                  # Streamlit frontend
├── requirements.txt        # Python dependencies
│
├── data/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│
├── models/
│   ├── pt_table.pkl        # Pivot table (book × user matrix)
│   ├── similarity.pkl      # Cosine similarity matrix
│   └── popular.pkl         # Top 50 popular books
│
└── notebooks/
    └── backend.ipynb       # Model training notebook
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Godcoder2005/Book-recommended-system.git
cd Book-recommended-system
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 Dependencies

```
streamlit
numpy
pandas
scikit-learn
pickle-mixin
```

---

## 📊 Dataset

- **Source**: [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
- **Books**: ~271,000 books
- **Ratings**: ~1.1 million ratings
- **Users**: ~278,000 users

After filtering:
- Books with **50+ ratings**
- Users who rated **200+ books**

---

## ✨ Features

- 🏠 **Home Page** — Top 50 most rated books with cover images, authors, and year
- 🔍 **Recommend Page** — Select any book and get 5 personalized recommendations
- 📞 **Contact Page** — About the developer

---

## 👨‍💻 Author

**Akshith Kumar**  
3rd Year CS Student @ IIIT Vadodara  
Passionate about AI, ML & Recommendation Systems

- 💼 [LinkedIn](https://www.linkedin.com/in/akshith-kumar-2982362b7)
- 💻 [GitHub](https://github.com/Godcoder2005)
- 📧 6305091489nani@gmail.com

---

## ⭐ If you found this useful, give it a star!
