import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import raw_parsers.ExcelParser as eParser
import random


class AdPropertiesParser:
    def __init__(self):
        self.baseParser = eParser.ExcelToPropertiesParser()

    # run from the project root directory
    def generate_data(self, num):
        propertiess = self.baseParser.parse("input/raw_data.xlsx","ads dimension (dim table)")
        ads = []
        for properties in propertiess:
            # quite some ad_revenue are None, so we need to filter them out
            if properties["ad_revenue"] is None or properties["baseline_st"] is None:
                continue
            if properties["punish_num"] is None:
                properties["punish_num"] = 0
            if properties["avg_ad_revenue"] is None:
                properties["avg_ad_revenue"] = 0
            ads.append(properties)
        selected_ads = random.sample(ads, num)
        self.ans = selected_ads  
        return selected_ads

# ads = AdPropertiesParser().generate_data(100)
# print(ads)