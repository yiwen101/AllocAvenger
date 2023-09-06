import ExcelParser as eParser


class ModeratorPropertiesParser:
    def __init__(self):
        self.baseParser = eParser.ExcelToPropertiesParser()

    # make sure the data input is valid, entry with empty values are either rewritten as null value of the type or discarded.
    def parse(self, path, sheet_name):
        propertiess = self.baseParser.parse(path, sheet_name)
        ans = []
        for properties in propertiess:
            if properties["Productivity"] is None or properties["Utilisation"] is None or properties["handling time"] is None or properties["accuracy"] is None:
                continue
            ans.append(properties)   
        return ans

'''
def moderatorPropertiesParserTest():
    parser = ModeratorPropertiesParser()
    testStr = "moderator//1689841547143170::market//SA&OM&BH&QA&JO::Productivity//286.2176::Utilisation//0.8124::handling time//123549::accuracy//0.99"
    property = parser.parse(testStr)
    ok = strPar.StrToPropertiesParser.propertyAssertHelper(
        ["moderator", "market", "Productivity", "Utilisation", "handling time",
         "accuracy"],
        [1689841547143170, ["SA", "OM", "BH", "QA", "JO"], 286.2176, 0.8124,
         123549, 0.99], property)
    if ok:
        print("moderatorPropertiesParserTest passed")
    else:
        print("moderatorPropertiesParserTest failed")
'''