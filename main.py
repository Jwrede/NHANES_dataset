
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.style as style 

style.use("seaborn-dark")

data = pd.read_csv(r"C:\Users\Jonathan\Desktop\coursera\Stats\week 2\data.csv")

def change_DMDMARTL_label():
    labels = ["Married", "Widowed", "Divorced", "Seperated", "Never married", 
              "Living with partner", "Refused", "Don't Know", "Missing"]
    values = [1,2,3,4,5,6,77,99,np.nan]
    data["DMDMARTL"].replace(values, labels, inplace = True)

change_DMDMARTL_label()

def frequency_tables():
    print("Frequency Table for the marital status:")
    print(data.DMDMARTL.value_counts(), "\n")
    print("Frequency Table for the marital status, males only:")
    print(data[data["RIAGENDR"] == 1].DMDMARTL.value_counts(), "\n")
    print("Frequency Table for the marital status, females only:")
    print(data[data["RIAGENDR"] == 2].DMDMARTL.value_counts(), "\n")
    
    print("Frequency Table for the marital status, 30 - 40 y.o.:")
    print(data[data["RIDAGEYR"].isin(range(30,40))].DMDMARTL.value_counts(), "\n")
    print("Frequency Table for the marital status, males only, 30 - 40 y.o.:")
    print(data[data["RIDAGEYR"].isin(range(30,40)) & (data["RIAGENDR"] == 1)].DMDMARTL.value_counts(), "\n")
    print("Frequency Table for the marital status, females only, 30 - 40 y.o.:")
    print(data[data["RIDAGEYR"].isin(range(30,40)) & (data["RIAGENDR"] == 2)].DMDMARTL.value_counts(), "\n")

def binned_frequency_tables_female():
    data["bins"] = pd.qcut(data[data["RIAGENDR"] == 2].RIDAGEYR, 10)
    bins = data.groupby("bins").DMDMARTL.value_counts().to_frame()
    bins.columns = ["Value"]
    _ = bins.pivot_table(index = "DMDMARTL", columns = "bins").fillna(0)
    
    for i in range(0, 10):
        _.iloc[:,i] /= _.iloc[:,i].sum()
        print(f"Frequency table for the marital status of females in the age interval {_.columns.get_level_values('bins')[i]}")
        print(_.iloc[:,i], "\n")

def plot_height_historgrams():
    data["BMXHT"].dropna(inplace = True)
    
    bins = np.arange(10,50,10)
    
    fig, axs = plt.subplots(2,2)
    
    axs[0,0].hist(data["BMXHT"], bins = bins[0], alpha = 0.5, color = "b")
    axs[0,0].set_title(f"{bins[0]} bins")
    axs[0,1].hist(data["BMXHT"], bins = bins[1], alpha = 0.5, color = "g")
    axs[0,1].set_title(f"{bins[1]} bins")
    axs[1,0].hist(data["BMXHT"], bins = bins[2], alpha = 0.5, color = "black")
    axs[1,0].set_title(f"{bins[2]} bins")
    axs[1,1].hist(data["BMXHT"], bins = bins[3], alpha = 0.5, color = "y")
    axs[1,1].set_title(f"{bins[3]} bins")
    
    fig.tight_layout()
    
    plt.show()

print(data["BPXSY1"] - data["BPXSY2"])

def show_test_differences():
    data.loc[:,["BPXSY1", "BPXSY2"]].dropna(inplace = True)
    sns.boxplot(data = (data["BPXSY1"]-data["BPXSY2"]))
    plt.show()

