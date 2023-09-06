import ExcelParser as eParser


class AdPropertiesParser:
    def __init__(self):
        self.baseParser = eParser.ExcelToPropertiesParser()
        self.ans = None
    # run from the project directory
    def parse(self):
        if self.ans is not None:
            return self.ans
        
        propertiess = self.baseParser.parse("input/raw_data.xlsx","ads dimension (dim table)")
        ans = []
        for properties in propertiess:
            # quite some ad_revenue are None, so we need to filter them out
            if properties["ad_revenue"] is None or properties["baseline_st"] is None:
                continue
            if properties["punish_num"] is None:
                properties["punish_num"] = 0
            if properties["avg_ad_revenue"] is None:
                properties["avg_ad_revenue"] = 0
            ans.append(properties)
        self.ans = ans
        return ans
            
               
        

#ads = AdPropertiesParser().parse()
#print(ads[0])
#print(ads[1])