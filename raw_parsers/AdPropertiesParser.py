import ExcelParser as eParser


class AdPropertiesParser:
    def __init__(self):
        self.baseParser = eParser.ExcelToPropertiesParser()
        
    def parse(self, advertisementStr):
        propertiess = self.baseParser.parse(advertisementStr)
        ans = []
        for properties in properties:
            # quite some ad_revenue are None, so we need to filter them out
            if properties["ad_revenue"] is None or properties["baseline_st"] is None:
                continue
            if properties["punish_num"] is None:
                properties["punish_num"] = 0
            if properties["avg_ad_revenue"] is None:
                properties["avg_ad_revenue"] = 0
            ans.append(properties)
        return ans
            
               
        

'''
def adPropertiesParserTest():
    parser = AdPropertiesParser()
    testStr = "p_data//20230807::ad_id//1747578422390810::delivery_country//US::queue_market//US&CA::punish_num//1::avg_ad_revenue//4796.25::ad_revenue//513217::start_time//10/24/2022 14:36::baseline_st//1.78"
    property = parser.parse(testStr)
    ok = strPar.StrToPropertiesParser.propertyAssertHelper(
        ["ad_id", "queue_market", "punish_num", "avg_ad_revenue", "ad_revenue",
         "baseline_st"],
        [1747578422390810, ["US", "CA"], 1, 4796.25, 513217, 1.78], property)
    if ok:
        print("adPropertiesParserTest passed")
    else:
        print("adPropertiesParserTest failed")
'''