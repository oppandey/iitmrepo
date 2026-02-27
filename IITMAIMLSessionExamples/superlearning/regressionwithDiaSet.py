# Starter Code for Regression Assignment 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#Available datasets for regression tasks
from sklearn.datasets import load_diabetes 
#from sklearn.datasets import load_boston    
#from sklearn.datasets import fetch_california_housing
#from sklearn.datasets import load_iris
#from sklearn.datasets import load_wine
#from sklearn.datasets import load_breast_cancer
#from sklearn.datasets import load_digits
#from sklearn.datasets import load_linnerud
#from sklearn.datasets import load_diabetes

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, Ridge, Lasso 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score 

# Load Diabetes dataset 
diabetes = load_diabetes() 
print(diabetes.DESCR)

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names) 
y = pd.Series(diabetes.target, name="target") 
# Split dataset for Tasks 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42) 
# You may start coding from here!  
#print(X.head(5))
#print(X.tail(5))
#print(X.describe())
#print(X.info())

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)

#model evaluation 
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')

plt.scatter(y_test, y_pred) 
plt.xlabel("Actual") 
plt.ylabel("Predicted") 
plt.title("Actual vs. Predicted") 
plt.show() 


feature = 'bmi' 
X_bmi = X[[feature]].values 
X_train_bmi, X_test_bmi, y_train_bmi, y_test_bmi = train_test_split(X_bmi, 
y, test_size=0.2, random_state=42) 

for degree in [2, 3, 5]: 
    poly = PolynomialFeatures(degree) 
    X_poly_train = poly.fit_transform(X_train_bmi) 
    X_poly_test = poly.transform(X_test_bmi) 

    model = LinearRegression() 
    model.fit(X_poly_train, y_train_bmi) 
    y_pred_train = model.predict(X_poly_train) 
    y_pred_test = model.predict(X_poly_test) 
    print(f"\nPolynomial Degree: {degree}") 
    print("Train R2:", r2_score(y_train_bmi, y_pred_train)) 
    print("Test R2:", r2_score(y_test_bmi, y_pred_test)) 
    plt.scatter(X_train_bmi, y_train_bmi, color='gray', alpha=0.5) 
    sorted_idx = np.argsort(X_train_bmi[:, 0]) 
    plt.plot(X_train_bmi[sorted_idx], y_pred_train[sorted_idx], 
    label=f"Degree {degree}") 
    plt.xlabel("BMI") 
    plt.ylabel("Target") 
    plt.legend() 
    plt.title(f"Polynomial Regression (degree {degree})") 
    plt.show() 

# Task 3: Overfitting 
# Use training vs. test R² to explain overfit vs. underfit 
# Degree 5 is likely to show overfitting (high train R², low test R²) 
# Task 4: Ridge and Lasso Regularization techniques to mitigate overfitting
alphas = [0.01, 0.1, 1, 10] 
for alpha in alphas: 
    ridge = Ridge(alpha=alpha) 
    ridge.fit(X_train, y_train) 
    print(f"Ridge (alpha={alpha}): Test R2: {ridge.score(X_test, y_test)}") 
    lasso = Lasso(alpha=alpha) 
    lasso.fit(X_train, y_train) 
    print(f"Lasso (alpha={alpha}): Test R2: {lasso.score(X_test, y_test)}")