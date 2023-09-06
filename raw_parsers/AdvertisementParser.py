import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import AdPropertiesParser as adPPar
from objects import Advertisement as ab


class AdvertisementParser:
    def __init__(self, estimator):
        self.propertiesParser = adPPar.AdPropertiesParser()
        self.estimator = estimator

    def parse(self, advertisementStr):
        properties = self.propertiesParser.parse(advertisementStr)
        return ab.Advertisement(properties, self.estimator)
