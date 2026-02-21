#create a python application that uses Supervised Learning to predict the price of a house based on its features such as size, number of bedrooms, and location.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('house_prices.csv')

# Select features and target variable
#X = data[['sqft_living', 'bedrooms', 'yr_built']]
y = data['price']

#Label encoding for location feature
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['city'] = le.fit_transform(data['city'])

# Update features to include the encoded location
X = data[['sqft_living', 'bedrooms', 'yr_built', 'city']]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

#print(y_pred)

#predict the price of a house with 2000 sqft, 3 bedrooms, built in 1990, and located in 'Redmond'
new_house = np.array([[2000, 3, 1990, le.transform(['Redmond'])[0]]])
predicted_price = model.predict(new_house)
print(f'The predicted price of the house is: ${predicted_price[0]:,.2f}')

#evaluation metrics of the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')