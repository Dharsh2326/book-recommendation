from flask import Flask, request, render_template
import pandas as pd
app = Flask(__name__)
books_df = pd.read_csv("books.csv", encoding='latin1')
book_tags_df = pd.read_csv("book_tags.csv", encoding='latin1')
tags_df = pd.read_csv("tags.csv", encoding='latin1')
@app.route('/')
def home():
    return render_template('index.html', recommendation=None)
@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood'].strip().lower()
    matching_tag = tags_df[tags_df['tag_name'].str.contains(mood, case=False)]
    if matching_tag.empty:
        return render_template('index.html', recommendation="No matching tag found.")
    tag_ids = matching_tag['tag_id'].tolist()
    matched_books = book_tags_df[book_tags_df['tag_id'].isin(tag_ids)]
    if matched_books.empty:
        return render_template('index.html', recommendation="No books found for this mood.")
    merged_df = pd.merge(matched_books, books_df, left_on='goodreads_book_id', right_on='book_id')
    top_n = merged_df.sort_values('count', ascending=False).head(10)
    top_book = top_n.sample(1)['title'].values[0]

    return render_template('index.html', recommendation=f"Recommended Book: {top_book}")

if __name__ == '__main__':
    app.run(debug=True)
