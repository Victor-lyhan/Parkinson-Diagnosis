import pandas as pd
import numpy as np
import re

vid = "p7v3" #TODO: Modify for diff video


def VidSessionCheck(video):
    sessionIndex = {1:24, 2:42, 3:60}
    vid_session = tuple(map(int,re.findall(r'\d+',video)))
    vs = (vid_session[0]-1,sessionIndex[vid_session[1]])
    return vs

def FoGperiodCheck(patient, session):
    df = pd.read_csv("Data/PDFEinfo.csv", encoding = 'latin-1', sep = ';')
    periodStr = df.iloc[patient, session].replace(" " , "")
    pairs = periodStr[1:-1].split(';')
    periods = []
    for pair in pairs:
        a,b = map(float, pair.split('-'))
        periods.append((a,b))
    return periods

P , S = VidSessionCheck(vid)
FoG_period = FoGperiodCheck(P,S)

file_path = f'Computer Vision/Results/{vid}_results.csv'
df = pd.read_csv(file_path, encoding='latin-1')

df_FoG = pd.DataFrame(columns = df.columns)
df_nonFoG = pd.DataFrame(columns = df.columns)

for period in range(0,len(FoG_period)):
    startTime = FoG_period[period][0]
    endTime = FoG_period[period][1]
    startRow = -1
    endRow = -1

    for frame in range(0,len(df)):
        if abs(df.iloc[frame,1] - startTime) < 0.04:
            startRow = frame
        elif abs(df.iloc[frame,1] - endTime) < 0.04:
            endRow = frame
            break
    if startRow != -1 and endRow != -1:
        df_FoG = pd.concat([df_FoG, df.iloc[startRow:endRow+1].dropna()] , ignore_index=True)

df_nonFoG = pd.concat([df_nonFoG, df[~df.isin(df_FoG.to_dict(orient='list')).all(axis=1)].dropna()], ignore_index=True)

df_FoG.to_csv(f'Computer Vision/Results/df_{vid}_FoG.csv', index=False)
df_nonFoG.to_csv(f'Computer Vision/Results/df_{vid}_nonFoG.csv', index=False)

print(f"Patient:{P}, session:{S}")
print(f"'{FoG_period}'")


