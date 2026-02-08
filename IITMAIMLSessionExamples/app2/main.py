import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Hello from app2!")
    data = pd.read_csv('chaisales.csv')
    print("Data loaded successfully.")
    print(data.head())
    print(data.describe())

    #data.plot(x='month', y='totalsales', kind='line')
    #plt.title('Chai Sales Over Months')
    #plt.xlabel('Month')
    #plt.ylabel('Sales')
    #plt.show()

    #plt.hist(data['totalsales'], bins=20, color='blue', alpha=0.7)
    #plt.plot(data['totalsales'], marker='o', linestyle='-', color='blue')
    plt.title('Distribution of Total Sales')
    plt.xlabel('Total Sales')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()