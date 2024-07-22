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
info_fogTime_index = {'1':25,'2':43,'3':61}
info_updrs3_index = {'1':14,'2':32,'3':50}

df_charac = df[df['statistic'].isin(characToCheck)].copy()
df_charac['FoG Ratio'] = [None] * len(df_charac) # Total time in fog(s) / 120s
df_charac['UPDRS-III'] = [None] * len(df_charac)

for video in len(df_charac):
    FoGRatio = 0
    UPDRS_III = 0
    

# .to_csv('Computer Vision/Results/all_stats_angularAcceleration.csv', index = False)
