import StrToPropertiesParser as strPar


class ModeratorPropertiesParser:
    def __init__(self):
        self.baseParser = strPar.StrToPropertiesParser()

    # make sure the data input is valid, entry with empty values are either rewritten as null value of the type or discarded.
    def parse(self, moderatorStr):
        properties = self.baseParser.parse(moderatorStr)
        properties["moderator"] = int(properties["moderator"])
        # this part, the one working on dealing iwth the input data should do extra work
        properties["market"] = properties["market"].split("&")
        # not sure why these two are in capital letters in the doc
        properties["Productivity"] = float(properties["Productivity"])
        properties["Utilisation"] = float(properties["Utilisation"])
        properties["handling time"] = float(properties["handling time"])
        properties["accuracy"] = float(properties["accuracy"])
        return properties


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
