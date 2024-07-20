import pandas as pd
import os

path_to_file = 'Computer Vision/Results/All/'

summary_list = []

for file_name in os.listdir(path_to_file):
    file_path = os.path.join(path_to_file, file_name)

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        df_desc = df.describe().T
        df_desc['file'] = file_name
        
        print(f"Processing file: {file_name}")
        print(f"DataFrame shape: {df.shape}")
        print(f"Statistics shape: {df_desc.shape}")
        
        summary_list.append(df_desc)

combined_desc = pd.concat(summary_list)

print(f"Combined description shape: {combined_desc.shape}")

combined_desc.to_csv('combined_summary.csv', index=False)
