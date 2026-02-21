#inplement KNN for the same dataset and compare the results with the previous models.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
# Load the dataset
data = pd.read_csv('house_prices.csv')

#label encodeing for city feature using OneHotEncoder
from sklearn.preprocessing import OneHotEncoder 
ohe = OneHotEncoder()
location_encoded = ohe.fit_transform(data[['city']]).toarray()
location_df = pd.DataFrame(location_encoded, columns=ohe.get_feature_names_out(['city']))

# Concatenate the encoded location features with the original features
X = pd.concat([data[['sqft_living', 'bedrooms', 'yr_built']], location_df], axis=1)
y = data['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=42)
# Create a KNN Regressor model 
model = KNeighborsRegressor(n_neighbors=5)
# Train the model on the training data
model.fit(X_train, y_train)
# Make predictions on the testing data
y_pred = model.predict(X_test)

#predict the price of a house with 2000 sqft, 3 bedrooms, built in 1990, and located in 'Redmond'
location_features = [1 if col == 'city_Redmond' else 0 for col in location_df.columns]
new_house = np.array([[2000, 3, 1990] + location_features])
predicted_price = model.predict(new_house)
print(f'The predicted price of the house is: ${predicted_price[0]:,.2f}')

#evaluation metrics of the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
