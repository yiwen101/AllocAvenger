class ModeratorStreamParser:
    def __init__(self, moderatorParser):
        self.moderatorParser = moderatorParser

    def parseFile(self, fileName):
        with open(fileName, "r") as file:
            # each line is one moderator
            lines = "".join(file.readlines()).strip().split("\n")
            Moderators = []
            for i in range(0, len(lines)):
                Moderators.append(self.moderatorParser.parse(lines[i]))
        file.close()
        return Moderators


def moderatorParserTest():
    class moveAdPArser:
        def parse(self, adStr):
            return adStr

    parser = ModeratorStreamParser(moveAdPArser())
    mds = parser.parseFile("inputs/moderatorsParserTest.txt")
    ok = len(mds) == 2 and mds[0] == "md1" and mds[1] == "md2"
    if ok:
        print("moderatorParserTest passed")
    else:
        print("moderatorParserTest failed")
