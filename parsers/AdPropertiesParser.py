import StrToPropertiesParser as strPar


class AdPropertiesParser:
    def __init__(self):
        self.baseParser = strPar.StrToPropertiesParser()

    # todo p_data//20230807, start_time//10/24/2022 14:36, last_pushnish_begin_date are left as string;
    def parse(self, advertisementStr):
        properties = self.baseParser.parse(advertisementStr)
        # In Python 3, the int type can represent integers of practically unlimited size, so there's usually no need to worry about the limitations of fixed-size integer types as you would in some other programming languages
        properties["ad_id"] = int(properties["ad_id"])
        properties["queue_market"] = properties["queue_market"].split("&")
        properties["punish_num"] = int(properties["punish_num"])
        properties["avg_ad_revenue"] = float(properties["avg_ad_revenue"])
        properties["ad_revenue"] = int(properties["ad_revenue"])
        properties["baseline_st"] = float(properties["baseline_st"])
        return properties


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
