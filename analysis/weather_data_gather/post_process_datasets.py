import pandas as pd
import numpy as np
import os


csvs = os.listdir('./DATASETS')

# confirm each files columns are same
cols = []
for csv in csvs: 
  df = pd.read_csv('./DATASETS/' + csv)
  if cols != list(df.columns):
    print(list(df.columns))
  cols = list(df.columns)

df_template = pd.read_csv("./DATASETS/aberdeenshire_aberdeen-mannofield-resr.csv",low_memory=False)
df_template[['wind_direction','wind_speed','air_temperature','dewpoint','wetb_temp','rltv_hum','ground_state_id','cld_ttl_amt_id']] = np.nan

df_avg = df_template.head(0)
for Y in [2005,2006,2007,2009,2010,2011,2012,2013,2014]:
    D_MAX = 365
    if Y % 4 == 0:
        D_MAX = 366
    for D in range(D_MAX):
        for H in range(24):
            row = pd.DataFrame([[H,D+1,Y]], columns=['hour','day_of_year','year'])
            df_avg = df_avg.append(row,ignore_index=True)


# get average dataset to fill nulls

csvs = os.listdir('./DATASETS/')
i = 0
for csv in csvs: 
  df = pd.read_csv('./DATASETS/' + csv,low_memory=False)
  df_avg = pd.concat((df_avg, df))
  df_avg = df_avg.groupby(['year','day_of_year','hour'])['wind_direction','wind_speed','air_temperature','dewpoint','wetb_temp','rltv_hum','ground_state_id','cld_ttl_amt_id'].mean().reset_index()
  i += 1
  print(str(i) + ' ',end='')
  
df_avg.to_csv("./DATASETS/avg.csv", index=False)