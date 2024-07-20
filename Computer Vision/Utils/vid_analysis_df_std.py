import pandas as pd
import numpy as np
import os
import pandas as pd
import os

# Path to the folder of csv files
path_to_folder = '../Computer Vision/Results/test/'

# Create an empty list
summary_list = []

# Iterate over each file in the folder
for file_name in os.listdir(path_to_folder):
    # Create directory for each individual video
    file_path = os.path.join(path_to_folder, file_name)

    # Ensure only CSV files are processed
    if file_path.endswith('.csv'):
        # Read the csv file, calculate the stats and add a column of which file the stats came from
        df = pd.read_csv(file_path)
        df_desc = df.describe().T
        df_desc['file'] = file_name
        
        # Print the shape of the DataFrame and the stats
        print(f"Processing file: {file_path}")
        print(f"DataFrame shape: {df.shape}")
        print(f"Statistics shape: {df_desc.shape}")
        
        # Append the statistic dataframe onto the list
        summary_list.append(df_desc)

# Combine the statistics dataframes from 'summary_list' into one df
combined_desc = pd.concat(summary_list)

# Print the shape of the combined DataFrame
print(f"Combined description shape: {combined_desc.shape}")

# Save to CSV
combined_desc.to_csv('combined_summary.csv', index=False)
