class strToPropertiesParser: 
    def parse(self,string):
        properties = {}
        property_strs = string.split(":")
        for i in range(0, len(property_strs)):
          property_str = property_strs[i]
          property = property_str.split("/")
          properties[property[0]] = property[1]
        return properties

def strToPropertiesParserTest():
    parser = strToPropertiesParser()
    testStr = "p1/v1:p2/v2:p3/v3"
    property = parser.parse(testStr)
    ok = property["p1"]=="v1" and property["p2"]=="v2" and property["p3"]=="v3"
    if ok:
        print("strToPropertiesParserTest passed")
    else:
        print("strToPropertiesParserTest passed")

class adPropertiesParser:
    def __init__(self):
        self.baseParser = strToPropertiesParser()
        
    def parse(advertisementStr):
        properties = strToPropertiesParser.parse(advertisementStr)
        # todo "p_date"]
        # In Python 3, the int type can represent integers of practically unlimited size, so there's usually no need to worry about the limitations of fixed-size integer types as you would in some other programming languages
        properties["ad_id"]=int(properties["ad_id"])
        return properties

class moderatorPropertiesParser:
    def __init__(self):
        self.baseParser = strToPropertiesParser()
        
    def parse(moderatorStr):
        properties = strToPropertiesParser.parse(moderatorStr)
        # do the type conversion
        return properties

class advertisementParser:
    def __init__(self, estimator):
        self.propertiesParser = adPropertiesParser()
        self.estimator = estimator
        
    def parse(self,advertisementStr):
        properties = adPropertiesParser.parse(advertisementStr)
        return Advertisement(properties, self.estimator)

class moderatorParser:
    def __init__(self, estimator):
        self.propertiesParser = moderatorPropertiesParser()
        self.estimator = estimator
        
    def parse(self,moderatorStr):
        properties = moderatorPropertiesParser.parse(moderatorStr)
        return Moderator(properties, self.estimator)

class advertisementStreamParser:
    def __init__(self, advertisementParser):
        self.advertisementParser = advertisementParser
    
    def parseFile(self, fileName):
        with open(fileName, "r") as file:
            lines = file.readlines()
            Advertismentss = []
            for i in range(0, len(lines)):
                Advertisments = self.parseAds(lines[i])
                Advertismentss.append(Advertisments)
            
            file.close()
            return Advertismentss
     
    def parseAds(self,adsStr):
        Advertisments = []
        adsStr = adsStr.split(" ")
        for i in range(0, len(adsStr)):
            input = adsStr[i]
            if input == "" or input == "\n" or input == " " or input == " \n":
                continue
            Advertisments.append(self.advertisementParser.parse(input.trim()))
        return Advertisments

class moderatorsParser:
    def __init__(self, moderatorParser):
        self.moderatorParser = moderatorParser
    
    def parseFile(self, fileName):
        with open(fileName, "r") as file:
            # each line is one moderator
            lines = file.readlines().replace("\n", "").trim()
            Moderators = []
            for i in range(0, len(lines)): 
                Moderators.append(self.moderatorParser.parse(lines[i]))
        file.close()
        return Moderators  

strToPropertiesParserTest()