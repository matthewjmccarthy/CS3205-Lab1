import pandas as pd
import re

# Read in the CSV file
df = pd.read_csv('HDI_filtered_data.csv')

# Drop any columns containing 'hdi' or 'country' in their names
df = df.drop(columns=[col for col in df.columns if 'hdi' in col or 'country' in col])

# Convert the dataframe to a string
df_string = df.to_string(index=False)

# Modify the string as required
df_lines = df_string.split('\n')
df_lines[0] = df_lines[0].split('iso3')[-1].lstrip()  # Remove up to and including 'iso3' on the first line
for i in range(1, len(df_lines)):
    for j in range(len(df_lines[i])):
        if df_lines[i][j].isalpha():
            df_lines[i] = df_lines[i][j:]  # Remove everything before the first alphabetical character on subsequent lines
            break
        
df_string = '\n'.join(df_lines)
df_string = df_string.replace('NaN', '0.0000')  # Replace 'NaN' with '0.0000'
df_string = re.sub('[ \t]+', ';', df_string)  # Replace groups of spaces/tabs with semicolons
df_string = df_string.lstrip() + '\n'  # Add a newline character to the end of the string

# Save the modified string to a file
with open('HDR_points_file.data', 'w') as f:
    f.write(df_string)