# app/feature_engineering.py

import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

# Step 1: Preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\S+@\S+', ' emailaddr ', text)
    text = re.sub(r'http\S+|www\S+', ' weblink ', text)
    text = re.sub(r'\d+', ' number ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Step 2: Load the combined dataset
def load_dataset():
    return pd.read_csv("data/combined_emails.csv")

# Step 3: Vectorize using TF-IDF
def extract_features(df):
    df['text'] = df['text'].astype(str)
    print(f"👉 Number of rows: {len(df)}")

    # Preprocess each row with progress logging
    processed_texts = []
    for i, text in enumerate(df['text']):
        if i % 1000 == 0:
            print(f"Processing row {i}/{len(df)}...")
        processed_texts.append(preprocess_text(text))
    
    df['text'] = processed_texts

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        stop_words='english'
    )
    X = vectorizer.fit_transform(df['text'])

    os.makedirs("models", exist_ok=True)
    joblib.dump(vectorizer, "models/tfidf_vectorizer.joblib")

    return X, df['label']

# Step 4: Save processed dataset
def save_transformed(X, y):
    from scipy import sparse
    sparse.save_npz("data/features.npz", X)
    y.to_csv("data/y_labels.csv", index=False)

if __name__ == "__main__":
    print("📄 Loading dataset...")
    df = load_dataset()

    print("🧹 Preprocessing & vectorizing...")
    X, y = extract_features(df)

    print("💾 Saving transformed features...")
    save_transformed(X, y)

    print("✅ Feature extraction complete!")
