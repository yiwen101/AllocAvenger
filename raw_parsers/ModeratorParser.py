import ModeratorPropertiesParser as modPPar
from objects import Moderator as mod


class ModeratorParser:
    def __init__(self):
        self.propertiesParser = modPPar.ModeratorPropertiesParser()

    def parse(self, moderatorStr):
        properties = modPPar.ModeratorPropertiesParser.parse(moderatorStr)
        return mod.Moderator(properties)
