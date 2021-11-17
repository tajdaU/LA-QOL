import pandas as pd

df = pd.read_csv('/Users/mythulam/Desktop/Masters/Fall_2021/3_Intro_to_DataAnalytics_in_Business/Course_Project/Data/Parcel/Assessor_Parcels_Data_2017.csv')

losangeles = df.loc[df.TaxRateArea_CITY.isin(['LOS ANGELES'])].copy()
losangeles.to_csv("losangeles_2017_v2.csv", index = False)

df = pd.read_csv('losangeles_2017_v2.csv')
LA_res = df.loc[df.GeneralUseType.isin(['Residential'])]
LA_res.to_csv('LA_res_2017_v2.csv', index = False)

COLUMNS = [ "AIN", 
            "RollYear",
            "AssessorID",
            "PropertyType",
            "SpecificUseType",
            "totBuildingDataLines",
            "YearBuilt",
            "EffectiveYearBuilt",
            "SQFTmain",
            "Bedrooms",
            "Bathrooms",
            "Units",
            "TotalValue",
            "Cluster",
            "ZIPcode5",
            "CENTER_LAT",
            "CENTER_LON"
            ]

df = pd.read_csv('LA_res_2017_v2.csv', skipinitialspace=True, usecols=COLUMNS)
df.to_csv('LA_res_selected_2017_v2.csv', index = False)