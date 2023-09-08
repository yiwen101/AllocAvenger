import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import raw_parsers.ExcelParser as eParser
import random

class ModeratorPropertiesParser:
    def __init__(self):
        self.baseParser = eParser.ExcelToPropertiesParser()
    
    # please call this from the root direcotry of the project
    # make sure the data input is valid, entry with empty values are either rewritten as null value of the type or discarded.
    def generate_data(self, num):
        propertiess = self.baseParser.parse("input/raw_data.xlsx","moderator dimension (dim table)")
        mods = []
        for properties in propertiess:
            if not isinstance(properties["Productivity"], float) or not isinstance(properties["Utilisation %"], float) or not isinstance(properties["handling time"], int) or not isinstance(properties["accuracy"], float):
                continue
            mods.append(properties) 
        selected_mods = random.sample(mods, num)
        self.ans = selected_mods  
        return selected_mods

# parser = ModeratorPropertiesParser()
# print(len(parser.generate_data(100)))