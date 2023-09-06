import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from objects.Moderator import Moderator

from raw_parsers.ModeratorPropertiesParser import ModeratorPropertiesParser

import json
import numpy as np
import pandas as pd

class ModeratorProducer():
    def __init__(self):
        pass
    
    def generate_data(self, num_samples):
        json_file_path = os.path.dirname(__file__) + '\\moderator_raw.json' 
        data_list = []
        with open(json_file_path, 'r') as f:
            for line in f:
                try:
                    json_object = json.loads(line)
                    data_list.append(json_object)
                except json.JSONDecodeError as e:
                    print(f"Skipping line due to JSONDecodeError: {e}")
        
        df = pd.DataFrame(data_list)
        numerical_cols_corrected = ['Productivity', 'Utilisation %', 'handling time', 'accuracy']
        for col in numerical_cols_corrected:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
        def generate_categorical(df, col, size):
            return df[col].dropna().sample(n=size, replace=True).values

        def generate_numerical(df, col, size):
            mean = df[col].mean()
            std = df[col].std()
            return np.random.normal(mean, std, size)

        synthetic_df = pd.DataFrame()
        
        categorical_cols = ['moderator', 'market']
        for col in categorical_cols:
            synthetic_df[col] = generate_categorical(df, col, num_samples)
        
        numerical_cols = ['Productivity', 'Utilisation %', 'handling time', 'accuracy']
        for col in numerical_cols:
            synthetic_df[col] = generate_numerical(df, col, num_samples)
        
        synthetic_df[numerical_cols] = synthetic_df[numerical_cols].apply(lambda x: np.maximum(0, x))    
        return synthetic_df

class ModeratorSampler:
    def __init__(self):
        self.propertiesProducer = ModeratorPropertiesParser
        self.ans = None
    
    def produce(self, num_samples):
        if self.ans is not None:
            return self.ans
        properties = self.propertiesProducer().parse()
        ans = []
        for p in properties:
            ans.append(Moderator(p))
        self.ans = ans
        return ans

def moderatorProducerTest():
    s = ModeratorSampler().produce(10)
    ok = isinstance(s[0], Moderator)
    if ok:
        print("moderatorProducerTest passed")
    else:
        print("moderatorProducerTest failed")
moderatorProducerTest()
def moderatorBuilderTest():
    builder = ModeratorProducer()
    ok = len(builder.generate_data(20)) == 20
    if ok:
        print("moderatorBuilderTest passed")
    else:
        print("moderatorBuilderTest failed")