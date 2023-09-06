import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import StandardScaler
from numpy.random import multivariate_normal

class AdvertisementBuilder():
    def __init__(self):
        pass

    def generate_data(self, num_samples):
        json_file_path = 'ads_raw.json' 
        data_list = []
        
        with open(json_file_path, 'r') as f:
            for line in f:
                try:
                    json_object = json.loads(line)
                    data_list.append(json_object)
                except json.JSONDecodeError as e:
                    print(f"Skipping line due to JSONDecodeError: {e}")
        
        df =  pd.DataFrame(data_list)
    
        def generate_categorical(df, col, size):
            return df[col].dropna().sample(n=size, replace=True).values
        
        def generate_numerical(df, col, size):
            mean = df[col].mean()
            std = df[col].std()
            return np.random.normal(mean, std, size).astype(np.int64)
        
        def generate_dependent_numerical(df, cols, size):
            scaled_df = df[cols].dropna()
            scaler = StandardScaler()
            scaled_df = scaler.fit_transform(scaled_df)
            cov_matrix = np.cov(scaled_df, rowvar=False)
            synthetic_data = multivariate_normal(np.zeros(len(cols)), cov_matrix, size)
            synthetic_data = scaler.inverse_transform(synthetic_data)
            return pd.DataFrame(synthetic_data, columns=cols)
        
        synthetic_df = pd.DataFrame()
        
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            synthetic_df[col] = generate_categorical(df, col, num_samples)
        
        independent_numerical_cols = ['punish_num', 'baseline_st', 'ad_revenue', 'avg_ad_revenue']
        for col in independent_numerical_cols:
            synthetic_df[col] = generate_numerical(df, col, num_samples)
        
        dependent_cols = ['latest_punish_begin_date', 'start_time']
        synthetic_dependent_data = generate_dependent_numerical(df, dependent_cols, num_samples)
        synthetic_df = pd.concat([synthetic_df, synthetic_dependent_data], axis=1)
        
        synthetic_df['ad_id'] = np.random.choice(df['ad_id'].dropna(), num_samples)
        synthetic_df['p_date'] = 20230807
        
        synthetic_df['punish_num'] = synthetic_df['punish_num'].apply(lambda x: max(0, int(round(x))))
        numerical_cols = synthetic_df.select_dtypes(include=[np.number]).columns
        synthetic_df[numerical_cols] = synthetic_df[numerical_cols].apply(lambda x: np.maximum(0, x))
        synthetic_df['latest_punish_begin_date'] = synthetic_df['latest_punish_begin_date'].astype(np.int64)
        synthetic_df['start_time'] = synthetic_df['start_time'].astype(np.int64)
        for col in ['latest_punish_begin_date', 'start_time']:
            synthetic_df[col] = pd.to_datetime(synthetic_df[col], unit='ms')
            
        return synthetic_df

def advertisementBuilderTest():
    builder = AdvertisementBuilder()
    ok = len(builder.generate_data(20)) == 20
    if ok:
        print("advertisementBuilderTest passed")
    else:
        print("advertisementBuilderTest failed")
