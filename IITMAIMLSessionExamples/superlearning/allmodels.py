#create a python application that uses Supervised Learning to predict the price of a house based on its features such as size, number of bedrooms, and location.
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

# Load the dataset
data = pd.read_csv('house_prices.csv')

# Select features and target variable
X = data[['sqft_living', 'bedrooms', 'yr_built']]
y = data['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Linear Regression model
#model = LinearRegression() #Prediction has been done using Linear Regression model in example1.py. Now we will use Logistic Regression model to predict the price of a house.
#model2 = LogisticRegression() #Classification algorithm, eg. Spam Detection, Customer Churn Prediction, etc.
model3 = DecisionTreeRegressor() #Regression algorithm, eg. House Price Prediction, Stock Price Prediction, etc.
model4 = RandomForestRegressor(n_estimators=100, random_state=42)   #Regression algorithm, eg. House Price Prediction, Stock Price Prediction, etc.
model5 = GaussianNB() #Classification algorithm, eg. Spam Detection, Customer Churn Prediction, etc., expects categorical features, so it may not perform well on this dataset without proper preprocessing.
model6 = KNeighborsRegressor(n_neighbors=5) #Regression algorithm, eg. House Price Prediction, Stock Price Prediction, etc.
model7 = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1) #Regression algorithm, eg. House Price Prediction, Stock Price Prediction, etc.

# Train the model on the training data
model3.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model3.predict(X_test)

#print(y_pred)

#predict the price of a house with 2000 sqft, 3 bedrooms, and built in 1990
new_house = np.array([[2000, 3, 1990]])
predicted_price = model3.predict(new_house)
print(f'The predicted price of the house is: ${predicted_price[0]:,.2f}')
