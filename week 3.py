import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.style.use('ggplot')

da = pd.read_csv(r"C:\Users\Jonathan\Desktop\coursera\Stats\week 2\NHANES_2015_2016.csv")


def plot_correlations():
    '''
    _______________________________________________________________________________________
    
    Plots different correlations of systolic and diastolic blood preasure tests. Also plots
    the log transformed versions of them.
    _______________________________________________________________________________________

    '''
    da.drop(da[(da["BPXDI1"] == 0) | (da["BPXDI2"] == 0)].index, inplace = True)
    
    fig, ax = plt.subplots(2,2)
    
    fig.suptitle("correlations of blood tests")
    
    corr_diastolic = da[["BPXDI1", "BPXDI2"]].corr()
    print(corr_diastolic)
    ax[0,0].scatter(da[["BPXDI1"]], da[["BPXDI2"]], c = "b", s = 5)
    ax[0,0].set_title("correlation diastolic tests", fontsize = 8)
    
    
    corr_systolic = da[["BPXSY1", "BPXSY2"]].corr()
    print(corr_systolic)
    ax[0,1].scatter(da[["BPXSY1"]], da[["BPXSY2"]], c = "g", s = 5)
    ax[0,1].set_title("correlation systolic tests", fontsize = 8)
    
    corr_sys_dia_1 = da[["BPXDI1", "BPXSY1"]].corr()
    print(corr_sys_dia_1)
    ax[1,0].scatter(da[["BPXDI1"]], da[["BPXSY1"]], c = "r", s = 5)
    ax[1,0].set_title("correlation 1. diastolic and 1. systolic tests", fontsize = 8)
    
    corr_sys_dia_2 = da[["BPXDI2", "BPXSY2"]].corr()
    print(corr_sys_dia_2)
    ax[1,1].scatter(da[["BPXDI2"]], da[["BPXSY2"]], c = "y", s = 5)
    ax[1,1].set_title("correlation 2. diastolic and 2. systolic tests", fontsize = 8)
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    
    
    fig, ax = plt.subplots(2,2)
    
    fig.suptitle("correlations of blood tests with log transformation")
    
    corr_diastolic = np.log(da[["BPXDI1", "BPXDI2"]]).corr()
    print(corr_diastolic)
    ax[0,0].scatter(np.log(da[["BPXDI1"]]), np.log(da[["BPXDI2"]]), c = "b", s = 5)
    ax[0,0].set_title("correlation diastolic tests", fontsize = 8)
    
    
    corr_systolic = np.log(da[["BPXSY1", "BPXSY2"]]).corr()
    print(corr_systolic)
    ax[0,1].scatter(np.log(da[["BPXSY1"]]), np.log(da[["BPXSY2"]]), c = "g", s = 5)
    ax[0,1].set_title("correlation systolic tests", fontsize = 8)
    
    corr_sys_dia_1 = np.log(da[["BPXDI1", "BPXSY1"]]).corr()
    print(corr_sys_dia_1)
    ax[1,0].scatter(np.log(da[["BPXDI1"]]), np.log(da[["BPXSY1"]]), c = "r", s = 5)
    ax[1,0].set_title("correlation 1. diastolic and 1. systolic tests", fontsize = 8)
    
    corr_sys_dia_2 = np.log(da[["BPXDI2", "BPXSY2"]]).corr()
    print(corr_sys_dia_2)
    ax[1,1].scatter(np.log(da[["BPXDI2"]]), np.log(da[["BPXSY2"]]), c = "y", s = 5)
    ax[1,1].set_title("correlation 2. diastolic and 2. systolic tests", fontsize = 8)
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    plt.show()

plot_corr_by_categories()

def plot_corr_by_categories():
    '''
    _______________________________________________________________________________________
    
    Plots different correlations between Diastolic and Systolic blood tests for male
    and female patients
    _______________________________________________________________________________________
    
    '''
    race_list = ["Mexican American", "Other Hispanic", "White", "Black", "Other Race"]
    gender_list = ["Male","Female"]
    color_list = ["b","y","g","r","black"]
    pivtab = da.set_index(["RIAGENDR","RIDRETH1"]).loc[:, ["BPXDI1","BPXSY1"]]
    
    fig, ax = plt.subplots(2,5)
    fig.suptitle("Diastolic vs. Systolic blood tests \n for different ethnicity groups", fontsize = 15)
    
    for i in range(0,2):
        for j in range(0,5):
            if i == 0:
                ax[i,j].set_xlabel("Diastolic")
                ax[i,j].xaxis.set_label_coords(0.5,-0.1)
            if i == 1:
                ax[i,j].set_xlabel(race_list[j], fontsize = 15)
            if j == 0:
                ax[i,j].set_ylabel(gender_list[i], rotation = 0, fontsize = 15)
                ax[i,j].yaxis.set_label_coords(-0.3,0.9)
            if j == 4:
                ax[i,j].set_ylabel("Systolic")
                ax[i,j].yaxis.set_label_position("right")
            ax[i,j].scatter(pivtab[(pivtab.index.get_level_values("RIAGENDR") == i+1) & (pivtab.index.get_level_values("RIDRETH1") == j+1)].BPXDI1, 
                            pivtab[(pivtab.index.get_level_values("RIAGENDR") == i+1) & (pivtab.index.get_level_values("RIDRETH1") == j+1)].BPXSY1,
                            c = color_list[j], s = 5, alpha = 0.8)
            ax[i,j].tick_params(axis = "both", which = "major", labelsize = 8)
 
    plt.show()
    
def BMI_to_educational_background():
    '''
    _______________________________________________________________________________________
    
    Plots different violin plots for the BMI distribution within different educational
    backgrounds for men and women.
    _______________________________________________________________________________________
    
    '''
    da.drop(da[da["DMDEDUC2"].isna()].index, axis = 0, inplace = True)
    da["DMDEDUC2"] = da["DMDEDUC2"].astype(int)
    values = [1,2,3,4,5,7,9]
    edu_lvl = ["Less Than 9th Grade","9-11th Grade", "High School Grad/GED", "Some College or AA degree", "College Graduate", "Refused", "Don't Know"]
    
    da["DMDEDUC2"] = da["DMDEDUC2"].replace(values, edu_lvl)
    
    fig,ax = plt.subplots(2,1)
    
    men = da[da["RIAGENDR"] == 1]
    women = da[da["RIAGENDR"] == 2]
    
    sns.violinplot(men.DMDEDUC2, men.BMXBMI, ax = ax[0])
    sns.violinplot(women.DMDEDUC2, women.BMXBMI, ax = ax[1])
    
    ax[0].set_ylabel("Men", rotation = 0, fontsize = 15)
    ax[0].yaxis.set_label_coords(-0.1,0.9)
    ax[0].set_xlabel("")
    ax[1].set_ylabel("Women", rotation = 0, fontsize = 15)
    ax[1].yaxis.set_label_coords(-0.11,0.9)
    ax[1].set_xlabel("Education Level")
    
    ax[0].tick_params(axis = "both", which = "major", labelsize = 10)
    ax[1].tick_params(axis = "both", which = "major", labelsize = 10)
    fig.suptitle("BMI by education level", fontsize = 20)
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    ax[1].tick_params(axis = "x", rotation=30)
    ax[0].tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)
    
    plt.show()

def BMI_to_age():
    '''
    _______________________________________________________________________________________
    
    Plots different violint plots for the BMI distribution within different age intervals
    for men and women.
    _______________________________________________________________________________________

    '''
    intervals = range(10, max(da.loc[:, "RIDAGEYR"])+1,10)
    
    da["Age intervals"] = pd.cut(da.loc[:, "RIDAGEYR"], intervals)
    
    Male = da[da["RIAGENDR"] == 1]
    Female = da[da["RIAGENDR"] == 2]
    
    fig,ax = plt.subplots(2,1)
    
    sns.violinplot(Male.loc[:, "Age intervals"], Male.BMXBMI, ax = ax[0])
    sns.violinplot(Female.loc[:, "Age intervals"], Female.BMXBMI, ax = ax[1])
    
    ax[0].set_ylabel("Male", rotation = 0, fontsize = 15)
    ax[0].yaxis.set_label_coords(-0.1,0.9)
    ax[0].set_xlabel("")
    ax[1].set_ylabel("Female", rotation = 0, fontsize = 15)
    ax[1].yaxis.set_label_coords(-0.11,0.9)
    ax[1].set_xlabel("Age Intervals")
    
    ax[0].tick_params(axis = "both", which = "major", labelsize = 10)
    ax[1].tick_params(axis = "both", which = "major", labelsize = 10)
    fig.suptitle("BMI by Age Intervals", fontsize = 20)
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    ax[1].tick_params(axis = "x", rotation=30)
    ax[0].tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)

def health_insurance_status_by_race():
    '''
    _______________________________________________________________________________________
    
    Prints a frequency table for the health insurance status within different ethicity
    groups
    _______________________________________________________________________________________
    '''
    race_values = [1,2,3,4,5]
    races = ["Mexican American", "Other Hispanic", "Non-Hispanic White", "Non-Hispanic Black", "Other Race"]
    da["RIDRETH1"].replace(race_values, races, inplace = True)
    
    insurance_values = [1,2,9]
    health_insurance_status = ["Yes", "No", "Don't know"]
    da["HIQ210"].replace(insurance_values, health_insurance_status, inplace = True)
    
    pivtab = da.pivot_table(index = "RIDRETH1", columns = "HIQ210", aggfunc = "size").fillna(0)
    pivtab.columns.name = "Insurance_status"
    pivtab.index.name = "Race"
    print(pivtab)