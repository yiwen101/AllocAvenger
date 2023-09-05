class StrToPropertiesParser:
    @staticmethod
    def parse(string):
        properties = {}
        property_strs = string.split("::")
        for i in range(0, len(property_strs)):
            property_str = property_strs[i]
            property = property_str.split("//")
            properties[property[0]] = property[1]
        return properties


def propertyAssertHelper(v1, v2, property):
    for i in range(0, len(v1)):
        if not property[v1[i]] == v2[i]:
            print("for " + v1[i],
                  "expect " + v2[i] + ", but get " + property[v1[i]])
            return False
    return True


def strToPropertiesParserTest():
    parser = StrToPropertiesParser()
    testStr = "p1//v1::p2//v2::p3//v3"
    property = parser.parse(testStr)
    ok = propertyAssertHelper(["p1", "p2", "p3"], ["v1", "v2", "v3"], property)
    if ok:
        print("strToPropertiesParserTest passed")
        return True
    else:
        print("strToPropertiesParserTest failed")
        return False
