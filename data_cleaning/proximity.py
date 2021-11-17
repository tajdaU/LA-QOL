import os
import pandas as pd
import geopandas as gpd

import numpy as np
import matplotlib.pyplot as plt

import folium
from folium import Marker, GeoJson

USER_PATH = "/Users/turtle/Desktop/IDA/_project_copy/LA-QOL/"

PATH_UNCLEAN = USER_PATH + "data/Assessor_Parcel_Data/_unclean/"
PATH_CLEAN = USER_PATH + "data/Assessor_Parcel_Data/_clean/"

PATH_PARKS = USER_PATH + "data/Parks/City_of_LA_Parks.shp"
PATH_BIKES = USER_PATH + "data/Bicycle/City_of_Los_Angeles_Bikeways.shp"
PATH_TRANSIT = USER_PATH + "data/Transit/Stations_All_0316.shp"
PATH_BORDER = USER_PATH + "data/City_Boundary/LA_County_City_Boundaries.shp"
PATH_BEACH = USER_PATH + "data/Beaches_and_Marinas/Beaches_and_Marinas.shp"

FILE = USER_PATH + "data/Assessor_Parcel_Data/_clean/LA_res_selected_2021_clean.csv"


def create_shp(file_name):
    parcels_df = pd.read_csv(FILE)

    parcels_gdf = gpd.GeoDataFrame(parcels_df, 
                    geometry = gpd.points_from_xy(parcels_df["CENTER_LAT"], parcels_df["CENTER_LON"]), 
                    crs = "EPSG:4326")
    
    parcels_gdf.to_file("ShapeFiles/" + file_name.split(".")[0] + ".shp")


def run_create_shp():
    for file_name in os.listdir(PATH_CLEAN):
        if file_name.endswith("csv"):
            print(file_name)
            create_shp(file_name)


def plot(buffer, buffer2, gdf_p, x):
    # check if this is LA location
    m = folium.Map(location = [34, -118.2], zoom_start = 9)

    for idx, row in gdf_p.iterrows():
        Marker([row['latitude'], row['longitude']]).add_to(m)
    
    buffer = buffer.to_crs(epsg = 4326)
    b = buffer.to_json()
    GeoJson(b).add_to(m)

    buffer2 = buffer2.to_crs(epsg = 4326)
    b2 = buffer2.to_json()
    GeoJson(b2).add_to(m)

    m.save("index2_" + x + ".html")


def not_important():
    # just some plots to see if coordinates make sense
    file_gdf = gpd.read_file(PATH_TRANSIT)
    parcels_df = pd.read_csv(FILE)
    border = gpd.read_file(PATH_BORDER)
    beach_gdf = gpd.read_file(PATH_BEACH)

    print(beach_gdf.geometry)
    beach_gdf = beach_gdf.to_crs(epsg = 4326)
    print(beach_gdf.geometry)

    # print(parcels_df.info())
    # print(file_gdf.columns)

    # renaming the columns
    # parcels_df.rename(
    #     columns = ({ "CENTER_LAT": 'latitude', 'CENTER_LON': 'longitude'}), 
    #     inplace =  True,
    # )

    # parcels_df.to_csv("_clean/new.csv")
    # file_gdf.plot()
    # plt.savefig("file.jpg")

    parcels_gdf = gpd.GeoDataFrame(parcels_df, 
                        geometry = gpd.points_from_xy(parcels_df["CENTER_LON"], parcels_df["CENTER_LAT"]), 
                        crs = "EPSG:4326")

    parcels_gdf.crs = {"init": "epsg:4326"}
    
    # parcels_gdf.plot()
    # plt.savefig("par.jpg")

    print(border.crs, beach_gdf.crs, file_gdf.crs, parcels_gdf.crs)

    # ugly plot
    f, ax = plt.subplots()
    border.plot(color = 'none', edgecolor = 'gainsboro', zorder = 3, ax = ax)
    parcels_gdf.plot(color = 'lightgreen', ax = ax)
    file_gdf.plot(color = 'red', markersize = 2, ax = ax)
    beach_gdf.plot(color = 'black', markersize = 4, ax = ax)
    plt.savefig("check.jpg")

    # check the coords
    # print(parcels_gdf.crs, file_gdf.crs)


def get_column(file_union, parcels_gdf_p):
    column = []
    for i in range(0, 694657):
        if file_union.contains(parcels_gdf_p.iloc[i].geometry):
            column.append(1)
        else:
            column.append(0)

    s = 0
    for val in column:
        s += val

    return column, s


def beach_prox(file_gdf, parcels_gdf, parcels_df, type_of_data):
    file_gdf_p = file_gdf.to_crs(epsg = 6423)
    print(3)
    parcels_gdf_p = parcels_gdf.to_crs(epsg = 6423)
    print(4)

    # 2 mile buffer
    two_mile_buffer = file_gdf_p.geometry.buffer(5280 * 2)
    print(5)

    # 4 mile buffer
    four_mile_buffer = file_gdf_p.geometry.buffer(5280 * 4)
    print(6)

    # plot(two_mile_buffer, four_mile_buffer, file_gdf, type_of_data)

    # union of polygons 
    file_2_union = two_mile_buffer.geometry.unary_union
    file_4_union = four_mile_buffer.geometry.unary_union
    print(7)

    # get binary column -> 1 if parcel in the radius, else 0
    column_2, s1 = get_column(file_2_union, parcels_gdf_p)
    print("How many parcels are in 2 mile radius:", s1)
    column_4, s2 = get_column(file_4_union, parcels_gdf_p)
    print("How many parcels are in 4 mile radius:", s2)

    # removing 1 in column_4 if parcel is in 2 mile radius already
    sc = np.add(column_2, column_4)
    sum_2 = np.where(sc == 2)

    for ix in sum_2[0]:
        column_4[ix] = 0

    s = 0
    for el in column_4:
        s += el

    print("How many parcels are in 4 mile radius (excluded 2 mile):", s)

    df = pd.DataFrame(parcels_df["AIN"])
    df[type_of_data + "_Buffer_2"] = column_2
    df[type_of_data + "_Buffer_4"] = column_4

    df.to_csv(type_of_data + "_buffer.csv", index = "False")


def prox(file_gdf, parcels_gdf, parcels_df, type_of_data):
    file_gdf_p = file_gdf.to_crs(epsg = 6423)
    print(3)
    parcels_gdf_p = parcels_gdf.to_crs(epsg = 6423)
    print(4)

    # 5 min buffer
    quarter_mile_buffer = file_gdf_p.geometry.buffer(5280 / 4)
    print(5)

    # 10 min buffer
    half_mile_buffer = file_gdf_p.geometry.buffer(5280 / 2)
    print(6)

    # union of polygons 
    file_5_union = quarter_mile_buffer.geometry.unary_union
    file_10_union = half_mile_buffer.geometry.unary_union
    print(7)

    # get binary column -> 1 if parcel in the radius, else 0
    column_5, s1 = get_column(file_5_union, parcels_gdf_p)
    print("How many parcels are in 5min radius:", s1)
    column_10, s2 = get_column(file_10_union, parcels_gdf_p)
    print("How many parcels are in 10min radius:", s2)

    # removing 1 in column_10 if parcel is in 5min radius already
    sc = np.add(column_5, column_10)
    sum_2 = np.where(sc == 2)

    for ix in sum_2[0]:
        column_10[ix] = 0

    s = 0
    for el in column_10:
        s += el

    print("How many parcels are in 10min radius (excluded 5min):", s)

    df = pd.DataFrame(parcels_df["AIN"])
    df[type_of_data + "_Buffer_5"] = column_5
    df[type_of_data + "_Buffer_10"] = column_10

    df.to_csv(type_of_data + "_buffer.csv", index = "False")


def run_proximity():
    parcels_df = pd.read_csv(FILE)

    parcels_gdf = gpd.GeoDataFrame(parcels_df, 
                        geometry = gpd.points_from_xy(parcels_df["CENTER_LON"], parcels_df["CENTER_LAT"]), 
                        crs = "EPSG:4326")

    parcels_gdf.crs = {"init": "epsg:4326"}
    print(1)

    transit_gdf = gpd.read_file(PATH_TRANSIT)
    bikes_gdf = gpd.read_file(PATH_BIKES)
    parks_gdf = gpd.read_file(PATH_PARKS)
    beach_gdf = gpd.read_file(PATH_BEACH)
    beach_gdf = beach_gdf.to_crs(epsg = 4326)
    print(2)

    print("Creating a buffer for transit data")
    prox(transit_gdf, parcels_gdf, parcels_df, "transit")

    print("Creating a buffer for bike data")
    prox(bikes_gdf, parcels_gdf, parcels_df, "bikes")

    print("Creating a buffer for park data")
    prox(parks_gdf, parcels_gdf, parcels_df, "parks")

    print("Creating a buffer for beach data")
    beach_prox(beach_gdf, parcels_gdf, parcels_df, "beach")


if __name__ == "__main__":
    # run_create_shp()
    # create_shp("LA_res_selected_2021_clean.csv")

    run_proximity()
    # not_important()
    
    pass
