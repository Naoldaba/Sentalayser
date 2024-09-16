## Sentiment Analyzer

# Overview

The Sentiment Analyzer is a machine learning application designed to analyze the sentiment of text data, specifically tailored for social media content. It employs natural language processing (NLP) techniques to categorize text into three sentiment classes: positive, negative, and neutral. This application provides an intuitive API for users to submit text and receive sentiment predictions, along with the ability to manage (CRUD) the text data.

# Features

- Sentiment Analysis: Classifies text into positive, negative, or neutral sentiment.
- CRUD Operations: Allows users to create, read, update, and delete text entries for analysis.
- Machine Learning Model: Utilizes a Logistic Regression model trained on a labeled dataset to make predictions.
- Data Preprocessing: Includes text normalization, tokenization, and stemming to enhance the model's performance.

# Technologies Used

- Python
- NLTK for Natural Language Processing
- Scikit-learn for Machine Learning
- Joblib for model serialization
- Pandas for data handling
- Flask for the web framework (if applicable)

# Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer
```

2. Download NLTK data: You may need to download the stopwords for NLTK:
```bash
import nltk
nltk.download('stopwords')
```

3. Run the application: If you have a Flask API, run the server:
```bash
python app.py
```

# CRUD Operations

Create
- Endpoint: POST /analyze
- Description: Submits a text for sentiment analysis.
- Request Body:
```json
{
  "content": "Your text goes here."
}
```

Response:
```json
{
  "content": "positive", // or "negative", "neutral"
}
```

Read
- Endpoint: GET /analyse/{id}
- Description: Retrieves the sentiment analysis result for a specific entry by ID.

Response:
```json
{
  "id": "59f49b5e-b7db-4d6c-9c1a-fb7899865663",
  "content": "Your text goes here.",
  "sentiment": "positive"
}
```

Update
- Endpoint: PUT /analyze/{id}
- Description: Updates the text entry for sentiment analysis.

Request Body:
```json
{
  "content": "Updated text goes here."
}
```

Response:
```json
{
  "content": "Text updated successfully."
}
```

Delete
- Endpoint: DELETE /analyze/{id}
- Description: Deletes a specific sentiment analysis entry by ID.

Response:
```json
{
  "content": "Entry deleted successfully."
}
```

## Model Details

# Model Training
The sentiment analysis model is based on a Logistic Regression algorithm, which is trained on a labeled dataset of social media texts. The training process involves the following steps:

1. Data Preprocessing: The text data undergoes normalization, including removing special characters, converting to lowercase, removing stop words, and stemming.

2. Vectorization: The processed text is transformed into a numerical format using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.

3. Training: The model is trained on the vectorized data, optimizing for accuracy in predicting the sentiment.