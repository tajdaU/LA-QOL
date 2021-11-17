import os
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

USER_PATH = "/Users/turtle/Desktop/IDA/_project_copy/LA-QOL/"

PATH_UNCLEAN = USER_PATH + "data/Assessor_Parcel_Data/_unclean/"
PATH_CLEAN = USER_PATH + "data/Assessor_Parcel_Data/_clean/"


def clean(file_name):
    # removes rows with 0 values in YearBuilt and EffectiveYearBuilt
    # removes rows with NaN values in zipcode5
    data = pd.read_csv(PATH_UNCLEAN + file_name)
    #print(data.shape[0])

    data = data[data['YearBuilt'] != 0]
    #print(data.shape[0])

    data = data[data['EffectiveYearBuilt'] != 0]
    #print(data.shape[0])

    data = data[data['ZIPcode5'].notna()]
    #print(data.shape[0])

    data = data[data['CENTER_LON'].notna()]
    data = data[data['CENTER_LAT'].notna()]

    if "Unnamed: 0" in data.columns:
        data.drop(labels = "Unnamed: 0", axis = 1)

    name = file_name.split(".")[0] + "_clean.csv"
    data.to_csv(PATH_CLEAN + name, index = False)


def start_cleaning():
    for file_name in os.listdir(PATH_UNCLEAN):
        if file_name.endswith("csv"):
            print(file_name)
            clean(file_name)


if __name__ == "__main__":
    # start_cleaning()
    file_name = "LA_res_selected_2017.csv"
    clean(file_name)

    pass