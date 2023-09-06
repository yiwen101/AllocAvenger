import pandas as pd

def adjust_columns(df):
    new_columns = df.iloc[0].values
    df = df.iloc[1:].reset_index(drop=True)
    df.columns = new_columns
    return df
  
def excel_to_json(excel_path):
  ads_df = pd.read_excel(excel_path, sheet_name='ads dimension (dim table)')
  moderator_df = pd.read_excel(excel_path, sheet_name='moderator dimension (dim table)')

  ads_df = adjust_columns(ads_df)
  moderator_df = adjust_columns(moderator_df)
    
  ads_json = ads_df.to_json(orient='records', lines=True)
  moderator_json = moderator_df.to_json(orient='records', lines=True)

  ads_json_path = 'ads_raw.json'
  moderator_json_path = 'moderator_raw.json'

  with open(ads_json_path, 'w') as f:
      f.write(ads_json)

  with open(moderator_json_path, 'w') as f:
      f.write(moderator_json)

import os
excel_to_json(os.getcwd() + "\\raw_data.xlsx")