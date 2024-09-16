import joblib
import os
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

model_path = os.path.join(os.path.dirname(__file__), "../bin/sentiment_model.joblib")
vectorizer_path = os.path.join(os.path.dirname(__file__), "../bin/tfidf_vectorizer.joblib")

model = joblib.load(model_path)
tfidf = joblib.load(vectorizer_path)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    text = text.split()
    text = [stemmer.stem(word) for word in text if word not in stop_words]
    return ' '.join(text)

def analyze_sentiment(text):
    processed_text = preprocess_text(text)

    X = tfidf.transform([processed_text])  
    prediction = model.predict(X)
    sentiment_map = {0: "negative", 2: "neutral", 4: "positive"}
    return sentiment_map.get(prediction[0], "unknown") 