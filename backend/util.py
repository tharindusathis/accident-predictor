import pickle
import pandas as pd
import os
import urllib.parse
import requests
import random


ball_tree_cluster = pickle.load(open("./models/ball_tree_cluster.tree", 'rb'))
gdf_df = pickle.load(open("./models/gdf_df.data", 'rb'))
dummy_weather_df = pickle.load(open("./models/dummy_weather.df", 'rb'))

def get_cluster(lat, lon):

    input_df  = pd.DataFrame(
        {'longitude': [
            lon
        ],'latitude': [
            lat
        ]})

    _, input_df['cluster_1'] = ball_tree_cluster.query(
        input_df[[ 'longitude','latitude']].values, # The input array for the query
        k=1, # The number of nearest neighbors
    )

    input_df['cluster_1'] = input_df['cluster_1'].apply(lambda x: gdf_df['cluster_1'].iloc[x])
    
    return input_df.iloc[0]['cluster_1']



'''
[Demostration purpose only] 
This give fake weather details to test the models

TODO: replace this with actual data from a weather API

Parameters:
air_temperature	    Air temperature	                [degC]
cld_ttl_amt_id	    Total cloud amount code	        [Oktas]
dewpoint	        Dewpoint temperature	        [degC]
ground_state_id	    Ground state code 
rltv_hum	        Calculated relative humidity	[%]
wind_direction  	wind direction	                [deg true]
wind_speed	        wind speed	                    [knots]

'''
def get_weather_data(cluster, date=-1):
    random.seed(cluster + date / 1000)
    SIZE = 78000
    data =  dummy_weather_df.loc[[random.randrange(SIZE)]].to_dict('records')[0]
    return (data)