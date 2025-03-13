####

# Each point in the data set corresponds to the purchase price of natural gas at the end of a month, from 31st October 2020 to 30th September 2024.
# Analyze the data to estimate the purchase price of gas at any date in the past and extrapolate it for one year into the future. 
# Your code should take a date as input and return a price estimate.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
import seaborn as sns 


#import the data and view it
natural_gas = pd.read_csv("Nat_Gas.csv", parse_dates=["Dates"])

# print(natural_gas.head(10))  #just to check the first 10 rows 
print (natural_gas.info())

def plot_line():
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14,6))
    sns.lineplot(data=natural_gas, x = 'Dates', y = 'Prices', label = "Monthly Prices", color='magenta')
    plt.xlabel('Monthly Data')
    plt.ylabel("Prices (usd?)")
    plt.show()
    
    return

plot_line()