import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import iqr
import numpy as np
import matplotlib.style as style 

style.use("seaborn-dark")

data = pd.read_csv(r"C:\Users\Jonathan\Desktop\coursera\Stats\week 2\data.csv")

def change_DMDMARTL_label():
    '''
    _________________________________________________________________________________________________
    
    Labels the DMDMARTL column that indicates the marital status  for better understanding
    _________________________________________________________________________________________________
    '''
    labels = ["Married", "Widowed", "Divorced", "Seperated", "Never married", 
              "Living with partner", "Refused", "Don't Know", "Missing"]
    values = [1,2,3,4,5,6,77,99,np.nan]
    data["DMDMARTL"].replace(values, labels, inplace = True)

def frequency_tables():
    '''
    _________________________________________________________________________________________________
    
    Prints frequency tables for marital status over 6 different groups:
        -All groups in the dataset
        -males only
        -females only
        -All groups in the dataset from age 30 to 40
        -males from age 30 to 40
        -famles from age 30 to 40
    _________________________________________________________________________________________________
    '''
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

def binned_frequency_tables(gender):
    '''
    _________________________________________________________________________________________________
    
    Takes in a gender and sums up the ages of the gender from the youngest to the oldest person
    in the dataset into 10 bins, then it prints out the frequency table for the different
    marital status for each interval which are described in proportions.
    Also returns the whole dataframe of frequency tables.
    
    Parameters:
        gender = 1 (male)
                 2 (female)
    _________________________________________________________________________________________________
    '''
    change_DMDMARTL_label()
    data["bins"] = pd.qcut(data[data["RIAGENDR"] == gender].RIDAGEYR, 10)
    bins = data.groupby("bins").DMDMARTL.value_counts().to_frame()
    bins.columns = ["Value"]
    _ = bins.pivot_table(index = "DMDMARTL", columns = "bins").fillna(0)
    
    for i in range(0, _.iloc[0].size):
        _.iloc[:,i] /= _.iloc[:,i].sum()
        genders = ["males","females"]
        print(f"Frequency table for the marital status of {genders[gender-1]} in the age interval {_.columns.get_level_values('bins')[i]}")
        print(_.iloc[:,i], "\n")
    return _

def plot_height_historgrams():
    '''
    _________________________________________________________________________________________________
    
    plots how different sizes of bins change the histogram of the height of the subjects
    _________________________________________________________________________________________________
    '''
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

def height_difference_by_gender():
    '''
    _________________________________________________________________________________________________
    
    First plots 2 boxplots for the height distributions in the dataset of males and females in two 
    different graphs, then they are plotted in the same graph to see the differences in the y-values
    _________________________________________________________________________________________________
    '''
    fig, axs = plt.subplots(2,1)
    sns.boxplot(data[data["RIAGENDR"] == 1].BMXHT, ax = axs[0])
    sns.boxplot(data[data["RIAGENDR"] == 2].BMXHT, ax = axs[1])
    plt.show()
    fig, axs = plt.subplots(1,1)
    sns.boxplot(data = (data[data["RIAGENDR"] == 1].BMXHT, data[data["RIAGENDR"] == 2].BMXHT))
    plt.show()

def show_test_differences():
    '''
    _________________________________________________________________________________________________
    
    Plots the absolute change between the first systolic blood pressure measurent and the second one
    and next to that boxplot two other ones that show each of the tests alone
    _________________________________________________________________________________________________
    '''
    data.loc[:,["BPXSY1", "BPXSY2"]].dropna(inplace = True)
    fig, axs = plt.subplots(1,2)
    sns.boxplot(data = (data["BPXSY1"]-data["BPXSY2"]), ax = axs[0])
    sns.boxplot(data = data.loc[:, ["BPXSY1", "BPXSY2"]], ax = axs[1])
    plt.show()

def education_household_relation():
    '''
    _________________________________________________________________________________________________
    
    Shows the  frequency table of household sizes for people within each educational attainment 
    category, the frequencies are shown as proportions.
    Also returns the dataframe that contains all these frequency tables.
    _________________________________________________________________________________________________
    '''
    education = ["Less than 9th grade", "9-11th grade (Includes 12th grade with no diploma)", 
                  "High school graduate/GED or equivalent", "Some college or AA degree", 
                  "College graduate or above", "Refused", "Don't Know", "Missing"]
    
    values = [1,2,3,4,5,7,9,np.nan]
    data["DMDEDUC2"].replace(values, education, inplace = True)
    
    _ = data.groupby(["DMDEDUC2", "DMDHHSIZ"]).size().to_frame()
    _.columns = ["Frequency"]
    _ = _.pivot_table(index = "DMDHHSIZ", columns = "DMDEDUC2", values = "Frequency").fillna(0)
    
    for i in range(0, _.iloc[0].size):
        _.iloc[:,i] /= _.iloc[:,i].sum()
        print(f"Frequency table for the size of a household in relation to the education level: {_.columns[i]}")
        print(_.iloc[:,i], "\n")
    return _

def group_data_PSU_MVU():
    '''
    _________________________________________________________________________________________________
    
    Groups the data into all different combinations of the Masked Variance Units (MVU) and the 
    Primary sampling units (Pseudo-PSU). 
    Creates a frequency table for each of these different groups containing the age, height and 
    BMI of the subjects and puts these into two different dataframes.
    The first one contains the mean of these features and the second one the IQR (InterQuartile Range).
    
    returns (grouped_data_mean, grouped_data_IQR)
    _________________________________________________________________________________________________
    '''
    data["RIAGENDR"].replace([1, 2],["male", "female"], inplace = True)
    _ = data.rename(columns = {"BMXBMI":"BMI", "BMXHT":"Height", "RIDAGEYR":"Age"}).fillna(0)
    grouped_data_mean = _.pivot_table(index = ["SDMVSTRA","SDMVPSU"], values = ["Age", "Height", "BMI"], columns = "RIAGENDR")
    
    grouped_data_IQR = _.pivot_table(index = ["SDMVSTRA","SDMVPSU"], values = ["Age", "Height", "BMI"], columns = "RIAGENDR", aggfunc = iqr)
    
    return grouped_data_mean, grouped_data_IQR

