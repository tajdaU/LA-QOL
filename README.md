# LA-QOL

# Frankfurt School of Finance and Management
# Class: Intro to Data Analytics

# Project: Real Estate Prices in Los Angeles, California, USA
# Members: Tajda Urankar, Thu Lam, Eduardo Garcia
# Date: 18-Nov-2021

This project explores the relationship between real estate prices and various parcel attributes including but not limited to square footage, year built, ZIP code, as well as proximity to parks, beaches, transit, and bicycle facilities in the City of Los Angeles, California.

This repository has four (4) sections:

1) DATA: All data used in the analysis, including attributes built by the team. Data files that are too large to push to the repository are in a OneDrive folder (https://fsstudentsde-my.sharepoint.com/:f:/g/personal/thu_lam_fs-students_de/EjVp8s6TpJFLvQZiKL7JzrsBlDXgy09mlh4M9KajsVnpqw?e=DL6M7I)

2) DATA CLEANING: All code written to clean and filter the data. 

3) MODEL: Code for the 
four (4) RANDOM FOREST REGRESSION models built to estimate value per square feet. 

4) VISUALIZATIONS: Tableau Workbook and R files used to create visualizations of the data. Tableau workbook is included in the OneDrive folder stated above.
 
-----------------------------------

DATA

* Assessor_Parcel_Data
    - All raw parcel data for the County of Los Angeles can be found in the OneDrive folder listed above.
    - LA_City_Parcels (Shapefile of parcels in the City of LA, created with QGIS, can be found in in the OneDrive folder)
    - _unclean (2017 - 2021 csv: City of LA parcel data before preprocessing with additional_clean.py)
    - _clean (2017 - 2021 csv: City of LA parcel data after preprocessing)
    - growth_rate.csv (calculated compound annual growth rate of Total Value from the last 5 years, calculated in project.ipynb)
    - Growth_Zip_Code_R.csv (used for R visualization listed below)
    - Metadata.xlsx (description of parcel attributes)

* Parks
    - County_of_LA (Shapefile of Countywide Parks and Open Space data, can be found in the OneDrive folder)
    - City_of_LA_Parks (Shapefile of Parks and Open Space in the City of Los Angeles, created with QGIS)

* Beaches_and_Marinas (Shapefile of beach locations)

* Bicycle (Shapefile of bike facilities in the City of Los Angeles)

* City_Boundary (Shapefile of city boundaries inside Los Angeles County)

* Transit (Shapefile of all LA Metro Rail Stations)

* Proximity
    - beach_buffer.csv (calculated with proximity.py)
    - bikes_buffer.csv (calculated with proximity.py)
    - parks_buffer.csv (calculated with proximity.py)
    - transit_buffer.csv (calculated with proximity.py)
    - yearRange_and_proximity.csv (new atrributes, calculated in project.ipynb)

-----------------------------------

DATA CLEANING

* cut_parcel_file.py - File used to filter the parcel data to Tax_Rate_Area = LOS ANGELES and only include the necessary attributes for analysis
* additional_clean.py - second round of cleaning the data
* proximity.py - file for calculating proximity
* QGIS was used to filter the Parcels and Parks shapefiles to only include features inside the City of Los Angeles.

-----------------------------------

MODEL

* project.ipynb (file that creates additional data - growth_rate.csv, yearRange_and_proximity.csv and creates the models for feature importance and prediction)

-----------------------------------

VISUALIZATION

* 2021_11_17_Two_Hist (R code for visualizing the parcel value increase from 2017 to 2021)
* City_of_LA_Parcel_Value_Visuals.twbx (Contains the rest of the project visualizations, can be found in the OneDrive folder)

-----------------------------------
