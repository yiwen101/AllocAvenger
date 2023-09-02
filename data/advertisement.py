import random

class Advertisment:
    def __init__(self, value, adType):
        self.value = value
        self.adType = adType
    def setID(self, id):
        self.id = id
    def getID(self):
        return self.id

class AdvertismentManager:
    def __init__(self, advertisementStream):
        self.advertisementStream = advertisementStream
        self.current_advertisments = {}
        self.timeRound = 0
        self.nextId = 0
    
    def update(self):
        if self.timeRound < len(self.advertisementStream):
            for ad in self.advertisementStream[self.timeRound]:
                ad.setID(self.nextId)
                self.current_advertisments[self.nextId] = ad
                self.nextId += 1
        
        self.timeRound += 1
            
    def get_advertisments(self):
        advertisements = []
        for _, value in self.current_advertisments.items():
            advertisements.append(value)
        return advertisements
    
    def markAsDone(self, id):
        self.current_advertisments.pop(id)
    
    def AllDone(self):
        return len(self.current_advertisments) == 0 and self.timeRound > 0

class MockAdvertisementBuilder:
    def build(self):
       type = random.randint(0, 10)
       value = random.randint(0, 100)
       return str(type) + "/" + str(value)
    
    def read(self, string):
       strings = string.split("/")
       return Advertisment(int(strings[1]), int(strings[0]))

