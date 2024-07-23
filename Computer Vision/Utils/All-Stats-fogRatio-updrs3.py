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

df = pd.read_csv('Computer Vision/Results/stats/all_stats_noOutliers_1000.csv') # All stats from all videos
info = pd.read_csv('Data/PDFEinfo.csv', encoding='latin-1', sep=';')
df_charac = df[df['statistic'].isin(characToCheck)].copy()

df_charac['FoG Ratio'] = [None] * len(df_charac) # FoG Ratio: Total time in fog(s) / 120s
df_charac['UPDRS-II'] = [None] * len(df_charac)
df_charac['UPDRS-III'] = [None] * len(df_charac)
df_charac['PIGD Score'] = [None] * len(df_charac)
df_charac['Dyskinesia Score'] = [None] * len(df_charac)
df_charac['MiniBestTest Score'] = [None] * len(df_charac)
df_charac['TUG time'] = [None] * len(df_charac)
df_charac['TUG dual-task time'] = [None] * len(df_charac)

info_fogTime_index = {1:25, 2:43, 3:61}
info_updrs3_index = {1:14, 2:32, 3:50}
info_updrs2_index = {1:13, 2:31, 3:49}
info_pigd_index = {1:15, 2:33, 3:51}
info_dyskinesia_index = {1:16, 2:34, 3:52}
info_miniBestTest_index = {1:21, 2:39, 3:57}
info_tug_index = {1:22, 2:40, 3:58}
info_tugDualTask_index = {1:23, 2:41, 3:59}

for video in range(len(df_charac)):
    file_name = df_charac.iloc[video,0]
    match = re.match(r'p(\d+)v(\d+)_results.csv', file_name)
    p = int(match.group(1))
    v = int(match.group(2))

    print(f'Video:{file_name}, patient:{p}, session:{v}') #Debug
    FoGTime = info.iloc[p-1,info_fogTime_index[v]]
    UPDRS_3 = info.iloc[p-1,info_updrs3_index[v]]
    UPDRS_2 = info.iloc[p-1,info_updrs2_index[v]]
    PIGD = info.iloc[p-1,info_pigd_index[v]]
    Dyskinesia = info.iloc[p-1,info_dyskinesia_index[v]]
    MiniBestTest = info.iloc[p-1,info_miniBestTest_index[v]]
    TUG = info.iloc[p-1,info_tug_index[v]]
    TUG_Dual = info.iloc[p-1,info_tugDualTask_index[v]]
    
    FoGRatio = round(float(FoGTime) / 120 * 100, 1) if FoGTime is not '-' else 0
    
    df_charac.iloc[video,-1] = TUG_Dual
    df_charac.iloc[video,-2] = TUG
    df_charac.iloc[video,-3] = MiniBestTest
    df_charac.iloc[video,-4] = Dyskinesia
    df_charac.iloc[video,-5] = PIGD
    df_charac.iloc[video,-6] = UPDRS_3
    df_charac.iloc[video,-7] = UPDRS_2
    df_charac.iloc[video,-8] = FoGRatio

df_charac.to_csv(f'Computer Vision/Results/stats-chosen/all_stats_noOutliers_{characToCheck[0]}_fogRatio_updrsIII.csv', index=False)
