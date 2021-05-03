import pickle
import pandas as pd
import numpy as np
import json
import util

model_random_forest = pickle.load(open("./models/rf_v1.model", 'rb'))
model_decision_tree = pickle.load(open("./models/dt_v1.model", 'rb'))

record_template = pickle.load(open("./models/record_v1.template", 'rb'))
record_template = record_template.head(0) 

predict_input_sample = {
    'engine_capacity_(cc)': 1598.0,
    'vehicle_type': 9.0,
    'latitude': 52.907427,
    'age_of_driver': 29.0,
    'longitude': 0.5031329999999999,
    'cluster_1': 20813.0,
    'day_of_year': 168.0,
    'rltv_hum': 93.65070004309445,
    'dewpoint': 13.473545391726475,
    'ground_state_id': 9.99945402758954,
    'age_of_vehicle': -1.0,
    'wind_speed': 2.761644671125486,
    'air_temperature': 14.473059052731935,
    'wind_direction': 111.18360952432366,
    'hour': 8.0,
    'cld_ttl_amt_id': 3.4569632403892405
    }


def predict_single(input):
    try:
        df = pd.DataFrame()
        df = record_template.append(input, ignore_index=True)
        pred_record = model_random_forest.predict(df)
        return not not pred_record[0]
    except Exception as e:
        print('Error', str(e))
        return False


def predict(input):
    common_record = {k:float(v) for k,v in input['common'].items()}
    weather_data = {} # cache weather data for a single cluster
    prev_cluster = -1
    accident_output = []
    for location in input['locations']:
        rec = common_record

        # location data
        rec['latitude'] = float(location['latitude'])
        rec['longitude'] = float(location['longitude'])
        rec['cluster_1'] = util.get_cluster(rec['latitude'], rec['longitude'])

        # dynamic data
        if prev_cluster != rec['cluster_1']:
            weather_data = util.get_weather_data(rec['cluster_1'])
            prev_cluster = rec['cluster_1']

        rec['air_temperature'] = weather_data['air_temperature']
        rec['cld_ttl_amt_id'] = weather_data['cld_ttl_amt_id']
        rec['dewpoint'] = weather_data['dewpoint']
        rec['ground_state_id'] = weather_data['ground_state_id']
        rec['rltv_hum'] = weather_data['rltv_hum']
        rec['wind_direction'] = weather_data['wind_direction']
        rec['wind_speed'] = weather_data['wind_speed']

        # print (json.dumps(rec, indent=2, default=str))

        if predict_single(predict_input_sample):
            accident_output.append({
                "latitude": rec['latitude'],
                "longitude": rec['longitude']
            })

    return accident_output

        
