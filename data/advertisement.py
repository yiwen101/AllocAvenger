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
        self.incompletedAds = {}
        self.unAssignedAds = {}
        self.timeRound = 0
        self.nextId = 0
        self.totalLost = 0
    
    def update(self):
        if self.timeRound < len(self.advertisementStream):
            for ad in self.advertisementStream[self.timeRound]:
                ad.setID(self.nextId)
                self.incompletedAds[self.nextId] = ad
                self.unAssignedAds[self.nextId] = ad
                self.nextId += 1
        self.timeRound += 1
            
    def get_advertisments(self):
        advertisements = []
        for _, value in self.unAssignedAds():
            advertisements.append(value)
        return advertisements
    
    def markAsDone(self, ads):
        for ad in ads:
            self.incompletedAds.pop(ad.getID())
    
    def markasAssigned(self, ads):
        for ad in ads:
            self.unAssignedAds.pop(ad.getID())
        
    def AllDone(self):
        return len(self.current_advertisments) == 0 and self.timeRound > 0
    
    def updateLoss(self, valueFunction):
        for ad in self.incompletedAds:
            self.totalLost += valueFunction(ad)
            
    def getLoss(self):
        return self.totalLost

class MockAdvertisementBuilder:
    def build(self):
       type = random.randint(0, 10)
       value = random.randint(0, 100)
       return str(type) + "/" + str(value)
    
    def read(self, string):
       strings = string.split("/")
       return Advertisment(int(strings[1]), int(strings[0]))

