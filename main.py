
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_csv(r"C:\Users\Jonathan\Desktop\coursera\Stats\week 2\data.csv")

def change_DMDMARTL_label():
    labels = ["Married", "Widowed", "Divorced", "Seperated", "Never married", 
              "Living with partner", "Refused", "Don't Know", "Missing"]
    values = [1,2,3,4,5,6,77,99,np.nan]
    data["DMDMARTL"].replace(values, labels, inplace = True)

change_DMDMARTL_label()

print("Frequency Table for the marital status:")
print(data.DMDMARTL.value_counts(), "\n")
print("Frequency Table for the marital status, males only:")
print(data[data["RIAGENDR"] == 1].DMDMARTL.value_counts(), "\n")
print("Frequency Table for the marital status, females only:")
print(data[data["RIAGENDR"] == 2].DMDMARTL.value_counts(), "\n")

print("Frequency Table for the marital status, 30 - 40 y.o.:")
print(data[data["RIDAGEYR"].isin(range(30,40))].DMDMARTL.value_counts(), "\n")
print("Frequency Table for the marital status, males only, 30 - 40 y.o.:")
print(data[data["RIDAGEYR"].isin(range(30,40)) & data["RIAGENDR"] == 1].DMDMARTL.value_counts(), "\n")
print("Frequency Table for the marital status, females only, 30 - 40 y.o.:")
print(data[data["RIDAGEYR"].isin(range(30,40)) & data["RIAGENDR"] == 2].DMDMARTL.value_counts(), "\n")