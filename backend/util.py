import pickle
import pandas as pd

ball_tree_cluster = pickle.load(open("./models/ball_tree_cluster.tree", 'rb'))
gdf_df = pickle.load(open("./models/gdf_df.data", 'rb'))

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

def get_weather_data(cluster):
    # todo
    return {
        "air_temperature": 14.473059052731935,
        "cld_ttl_amt_id": 3.4569632403892405,
        "dewpoint": 13.473545391726475,
        "ground_state_id": 9.99945402758954,
        "rltv_hum": 93.65070004309445,
        "wind_direction": 111.18360952432366,
        "wind_speed": 2.761644671125486
    }
