#implement decision tree algorithm using house_prices.csv file to predict the price of a house based on its features such as size, number of bedrooms, and location.
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('house_prices.csv')
#use onehot encoding for City feature
city_df = pd.get_dummies(data['city'], prefix='city')

# Select features and target variable
X = pd.concat([data[['sqft_living', 'bedrooms', 'yr_built']], city_df], axis=1)
y = data['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Decision Tree Regressor model
model = DecisionTreeRegressor()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

#predict the price of a house with 2000 sqft, 3 bedrooms, built in 1990, and located in 'Redmond'
location_features = [1 if col == 'city_Redmond' else 0 for col in city_df.columns]
new_house = np.array([[2000, 3, 1990] + location_features])
predicted_price = model.predict(new_house)
print(f'The predicted price of the house is: ${predicted_price[0]:,.2f}')

#evaluation metrics of the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')