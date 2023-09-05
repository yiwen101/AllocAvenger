class AdvertisementStreamParser:
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

    def parseAds(self, adsStr):
        Advertisments = []
        adsStr = adsStr.split("ADEND!")
        for i in range(0, len(adsStr)):
            input = adsStr[i]
            if input == "" or input == "\n" or input == " " or input == " \n":
                continue
            Advertisments.append(self.advertisementParser.parse(input.strip()))
        return Advertisments


def advertisementStreamParserTest():
    class moveAdPArser:
        def parse(self, adStr):
            return adStr

    parser = AdvertisementStreamParser(moveAdPArser())
    adss = parser.parseFile("inputs/adStreamParserTest.txt")
    ok = len(adss) == 2 and len(adss[1]) == 3 and adss[0][0] == "ad1" and \
         adss[1][2] == "ad6"
    if ok:
        print("advertisementStreamParserTest passed")
    else:
        print("advertisementStreamParserTest failed")
