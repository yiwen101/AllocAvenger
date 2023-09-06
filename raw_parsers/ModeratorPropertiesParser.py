import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import raw_parsers.ExcelParser as eParser


class ModeratorPropertiesParser:
    def __init__(self):
        self.baseParser = eParser.ExcelToPropertiesParser()
        self.ans = None
    
    # please call this from the root direcotry of the project
    # make sure the data input is valid, entry with empty values are either rewritten as null value of the type or discarded.
    def parse(self):
        if self.ans is not None:
            return self.ans
        propertiess = self.baseParser.parse("input/raw_data.xlsx","moderator dimension (dim table)")
        ans = []
        for properties in propertiess:
            if not isinstance(properties["Productivity"], float) or not isinstance(properties["Utilisation %"], float) or not isinstance(properties["handling time"], int) or not isinstance(properties["accuracy"], float):
                continue
            ans.append(properties) 
        self.ans = ans  
        return ans

#parser = ModeratorPropertiesParser()
#print(parser.parse()[0]["accuracy"])