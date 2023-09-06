import pandas as pd

class ExcelToPropertiesParser:
    def __init__(self):
        self.dicts = None
    
    def parse(self, path, sheet_name):
        if self.dicts is None:
             df = pd.read_excel(path, sheet_name)
             df.columns = df.iloc[0]
             df = df[1:].reset_index(drop=True)
             dicts = df.to_dict('records')
             self.dicts = dicts
        return self.dicts
