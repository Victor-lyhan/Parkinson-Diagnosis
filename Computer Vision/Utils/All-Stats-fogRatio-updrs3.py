'''
Patient Data:

Select a certain characteristic in the "all_stats" dataframe and incoporate FoG Time and UPDRS-III from the PDFEinfo.csv for comparison
Ultimately forming:

File, Statistic, (stats), FoG Ratio, UPDRS-III Score

'''

import pandas as pd
import numpy as np
import re
import os

characToCheck = ['linear_acceleration'] #Angular Acceleration 

df = pd.read_csv('Computer Vision/Results/all_stats.csv') # All stats from all videos
info = pd.read_csv('Data/PDFEinfo.csv', encoding='latin-1', sep=';')
df_charac = df[df['statistic'].isin(characToCheck)].copy()

df_charac['FoG Ratio'] = [None] * len(df_charac) # Total time in fog(s) / 120s
df_charac['UPDRS-III'] = [None] * len(df_charac)

info_fogTime_index = {1:25, 2:43, 3:61}
info_updrs3_index = {1:14, 2:32, 3:50}

for video in range(len(df_charac)):
    file_name = df_charac.iloc[video,0]
    match = re.match(r'p(\d+)v(\d+)_results.csv', file_name)
    p = int(match.group(1))
    v = int(match.group(2))

    print(f'Video:{file_name}, patient:{p}, session:{v}') #Debug
    FoGTime = info.iloc[p-1,info_fogTime_index[v]]
    UPDRS_3 = info.iloc[p-1,info_updrs3_index[v]]
    
    FoGRatio = round(float(FoGTime) / 120 * 100, 1) if FoGTime is not '-' else 0
    
    df_charac.iloc[video,-2] = FoGRatio
    df_charac.iloc[video,-1] = UPDRS_3

df_charac.to_csv(f'Computer Vision/Results/all_stats_{characToCheck}_fogRatio_updrsIII.csv', index=False)
