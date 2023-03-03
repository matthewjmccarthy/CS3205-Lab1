import pandas as pd

def create_HDI_date(data: str, save_to: str):
    df = pd.read_csv(f'{data}')
    # Extract the desired columns into a new dataframe
    new_df = df[['iso3', 'country', 'hdi_2021', 'gdi_2021', 'le_f_2021', 'le_m_2021', 'mys_f_2021', 'mys_m_2021', 'gni_pc_f_2021', 'gni_pc_m_2021', 'ineq_le_2021', 'ineq_edu_2021', 'ineq_inc_2021']]
    # Add a new column called 'Label' based on the 'hdi' values
    new_df['Label'] = pd.cut(new_df['hdi_2021'], bins=[0, 0.55, 0.7, 0.8, 1], labels=[4, 3, 2, 1])
    # Remove rows where the 'iso3' column starts with 'ZZ' (OPTIONAL)
    new_df = new_df[~new_df['iso3'].str.startswith('ZZ')]
    new_df.to_csv(f'{save_to}')
    
def append_2021_HDI_data(original_data, data_2021):
    df1 = pd.read_csv(f'{original_data}', index_col='Country_code')
    df2 = pd.read_csv(f'{data_2021}', index_col='iso3')

    # select the columns we want to append from df2 (Region is Optional and only used for testing)
    df2 = df2[['region', 'hdi_2020', 'hdi_2021']]

    # append the columns to df1, inserting them at position 31 and 32
    #df1.insert(0, 'region', df2['region'])
    df1.insert(31, '2020', df2['hdi_2020'])
    df1.insert(32, '2021', df2['hdi_2021'])

    df1.to_csv('merged_file.csv')
    
