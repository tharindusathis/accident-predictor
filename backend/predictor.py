import pickle
import pandas as pd
import numpy as np

logreg_model = pickle.load(open("./models/logreg_v0.1.model", 'rb'))
logreg_template = pickle.load(open("./models/logreg_v0.1.template", 'rb'))

predict_input_sample = {
    'Longitude': -1.528166,
    'Latitude': 54.519576,
    'Day_of_Week': 4.0,
    'Speed_limit': 30.0,
    'Urban_or_Rural_Area': 1.0,
    'Year': 2006.0,
    'Hour': 9.0,
    'Day_of_Year': 18.0,
    'Cluster_1': 11612.0,
    'Vehicle_Type': 9.0,
    'Sex_of_Driver': 1.0,
    'Age_of_Driver': 68.0,
    'Engine_Capacity_(CC)': -1.0,
    'Age_of_Vehicle': -1.0,
    'Driver_Home_Area_Type': 1.0,
    'Road_Type_Dual carriageway': 0,
    'Road_Type_One way street': 0,
    'Road_Type_Roundabout': 0,
    'Road_Type_Single carriageway': 1,
    'Road_Type_Slip road': 0,
    'Road_Type_Unknown': 0,
    'Light_Conditions_Darkeness: No street lighting': 0,
    'Light_Conditions_Darkness: Street lighting unknown': 0,
    'Light_Conditions_Darkness: Street lights present and lit': 0,
    'Light_Conditions_Darkness: Street lights present but unlit': 0,
    'Light_Conditions_Daylight: Street light present': 1,
    'Weather_Conditions_Fine with high winds': 0,
    'Weather_Conditions_Fine without high winds': 1,
    'Weather_Conditions_Fog or mist': 0,
    'Weather_Conditions_Other': 0,
    'Weather_Conditions_Raining with high winds': 0,
    'Weather_Conditions_Raining without high winds': 0,
    'Weather_Conditions_Snowing with high winds': 0,
    'Weather_Conditions_Snowing without high winds': 0,
    'Road_Surface_Conditions_Dry': 0,
    'Road_Surface_Conditions_Flood (Over 3cm of water)': 0,
    'Road_Surface_Conditions_Frost/Ice': 0,
    'Road_Surface_Conditions_Snow': 0,
    'Road_Surface_Conditions_Wet/Damp': 1
}


def predict_single(input):
    test_record = logreg_template
    test_record = test_record.head(0)
    try:
        test_record = test_record.append(input, ignore_index=True)
        pred_record = logreg_model.predict(test_record)
        return {'Accidents': pred_record.tolist()}
    except Exception as e:
        return {'Error': str(e)}
