import random

class MockAdvertisment:
    def __init__(self, value, adType):
        self.value = value
        self.adType = adType
    def setID(self, id):
        self.id = id
    def getID(self):
        return self.id
    def toString(self):
        return "type: " + str(self.adType) + "/" + str(self.value)

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
            
    def getAdvertisements(self):
        return self.unAssignedAds.values()
        
    
    def markAsDone(self, ads):
        for ad in ads:
            self.incompletedAds.pop(ad.getID())
    
    def markAsAssigned(self, ads):
        for ad in ads:
            self.unAssignedAds.pop(ad.getID())
        
    def allDone(self):
        return len(self.incompletedAds) == 0 and self.timeRound > 0
    
    def updateLoss(self, valueFunction):
        for ad in self.incompletedAds.values():
            self.totalLost += valueFunction(ad)
            
    def getLoss(self):
        return self.totalLost

class MockAdvertisementBuilder:
    def build(self):
       type = random.randint(0, 9)
       value = random.randint(0, 100)
       return str(type) + "/" + str(value)
    
    def read(self, string):
       strings = string.split("/")
       adType = int(strings[0])
       value = int(strings[1])
       return MockAdvertisment(value, adType)

class AdvertisementBuilder:
     def read(self, string):
       properties = {}
       property_strs = string.split("/")
       for i in range(0, len(property_strs)):
          property_str = property_strs[i]
          property = property_str.split(":")
          properties[property[0]] = property[1]
        
       return Moderator(properties, self.estimator)
   
class Advertisement:
    def __init__(self, properties, estimateValue):
         self.properties = properties
         self.estimateValue = estimateValue
         self.accumulatedLoss = 0
         self.isDone = False
         self.isAssigned = False
    
    def isDone(self):
        return self.isDone
    
    def isAssigned(self):
        return self.isAssigned
    
    def assign(self):
        self.isAssigned = True
    
    def done(self):
        self.isDone = True
    
    def updateLoss(self):
        self.accumulatedLoss += self.estimateValue(self.properties)
         
    def getLoss(self):
        return self.accumulatedLoss

