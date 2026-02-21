#Classification implementation using Naive Bayes algorithm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset of sentiment analysis of movie reviews
data = pd.read_csv('movie_reviews.csv')

# Select features and target variable
X = data['review'] #Feature: text reviews
y = data['sentiment_label'] #Target variable: sentiment label (positive or negative)

# Convert text to numerical features using TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = \
        train_test_split(X_vectorized, y, test_size=0.3, random_state=42)

# Create a Naive Bayes model
model = MultinomialNB()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Predict the sentiment of a new movie review
new_review = ['This movie was pathetic, did not like it!']
new_review_vectorized = vectorizer.transform(new_review)
predicted_sentiment = model.predict(new_review_vectorized)
print(f'The predicted sentiment of the review is: {predicted_sentiment[0]}')

#evaluation metrics of the model
#from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
#accuracy = accuracy_score(y_test, y_pred)
#print(f'Accuracy: {accuracy:.2f}')
#print('Classification Report:')
#print(classification_report(y_test, y_pred))
#print('Confusion Matrix:')
#print(confusion_matrix(y_test, y_pred))
