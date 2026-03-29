import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------------- LOAD DATA ---------------- #
pt_table = pickle.load(open('models/pt_table.pkl', 'rb'))
similarity_search = pickle.load(open('models/similarity.pkl', 'rb'))
popular_df = pickle.load(open('models/popular.pkl', 'rb'))
books = pd.read_csv('data/Books.csv', low_memory=False)

# Strip whitespace from pt_table index
pt_table.index = pt_table.index.str.strip()
popular_df.columns = popular_df.columns.str.strip()

# ---------------- RECOMMEND FUNCTION ---------------- #
def recommend(book_name):
    if book_name not in pt_table.index:
        return []

    index = np.where(pt_table.index == book_name)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_search[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []

    for i in similar_items:
        book_title = pt_table.index[i[0]]

        temp_df = books[
            books['Book-Title'].str.lower().str.strip() ==
            book_title.lower().strip()
        ]

        if not temp_df.empty:
            data.append({
                "title": book_title,
                "author": temp_df['Book-Author'].values[0],
                "year": temp_df['Year-Of-Publication'].values[0],
                "image": temp_df['Image-URL-M'].values[0]
            })
        else:
            data.append({
                "title": book_title,
                "author": "Unknown",
                "year": "N/A",
                "image": "https://via.placeholder.com/120x180?text=No+Cover"
            })

    return data


# ---------------- PAGE SETUP ---------------- #
st.set_page_config(page_title="Book Recommender", layout="wide")

st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🔍 Recommend", "📞 Contact"])

# ---------------- HOME PAGE ---------------- #
if page == "🏠 Home":

    st.title("📚 Top 50 Books")
    st.markdown("### Most popular books based on ratings ⭐")

    top_books = popular_df.sort_values(by='num_ratings', ascending=False).head(50)

    for i in range(0, 50, 5):
        cols = st.columns(5)
        for j in range(5):
            if i + j < len(top_books):
                with cols[j]:
                    st.image(top_books.iloc[i + j]['Image-URL-M'], width=120)
                    st.markdown(f"**{top_books.iloc[i + j]['Book-Title']}**")
                    st.caption(top_books.iloc[i + j]['Book-Author'])
                    st.caption(f"Year: {top_books.iloc[i + j]['Year-Of-Publication']}")

# ---------------- RECOMMEND PAGE ---------------- #
elif page == "🔍 Recommend":

    st.title("🔍 Book Recommendation System")

    book_list = pt_table.index.values
    selected_book = st.selectbox("Choose a book", book_list)

    if st.button("Recommend"):

        # Debug lines - remove after confirming it works
        st.write("Book selected:", selected_book)
        st.write("In pt_table?", selected_book in pt_table.index)

        recommendations = recommend(selected_book)

        if recommendations:
            st.subheader("✨ Recommended Books")
            cols = st.columns(5)
            for i, book in enumerate(recommendations):
                with cols[i]:
                    st.image(book['image'], width=130)
                    st.markdown(f"**{book['title']}**")
                    st.caption(book['author'])
                    st.caption(f"Year: {book['year']}")
        else:
            st.error("No recommendations found")

# ---------------- CONTACT PAGE ---------------- #
elif page == "📞 Contact":

    st.title("📞 Contact")
    st.markdown("""
    ### 👋 About Me
    Hi, I'm **Akshith Kumar**  
    Passionate about AI & Machine Learning 🚀  
    Built this Book Recommendation System using collaborative filtering.
    ---
    ### 📬 Get in Touch
    📧 Email: 6305091489nani@gmail.com  
    💼 LinkedIn: https://www.linkedin.com/in/akshith-kumar-2982362b7  
    ---
    ### 🧠 Skills
    - Machine Learning  
    - Deep Learning  
    - Recommendation Systems  
    - Python & Data Science  
    ---
    ⭐ If you like this project, feel free to connect!
    """)