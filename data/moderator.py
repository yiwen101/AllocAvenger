import random


class MockModerator:

    def __init__(self, ability):
         self.Ability = ability
         self.workOn = None
         self.expectedRemainingTime = 0
         self.workcount = 0
         self.totalWorkTime = 0
        
    

    def getAdTimeEstimate(self, advertisement):
        return self.Ability[advertisement.adType]
    
    def isIdle(self):
        return self.workOn == None
    
    def assign(self, advertisement):
        if(not self.isIdle()):
            raise Exception("Moderator is not idle")
        self.workOn = advertisement
        self.expectedRemainingTime = self.getAdTimeEstimate(advertisement)

    def work(self, completedTasks):
        self.totalWorkTime += 1
        if(not self.isIdle()):
          self.expectedRemainingTime -= 1
          self.workcount += 1
          if(self.expectedRemainingTime == 0):
              completedTasks.append(self.workOn)
              self.workOn = None

class ModeratorManager:
    moderators = []
    
    def __init__(self, moderators):
        self.moderators = moderators
    
    def getModerators(self):
       return self.moderators

    def assign(self,advertisements, ids):
        for i in range(0, len(ids)):
            moderator = self.moderators[ids[i]]
            advertisement = advertisements[i]
            moderator.assign(advertisement)
                 
    def work(self):
        completedTasks = []
        for moderator in self.moderators:
            moderator.work(completedTasks)
        return completedTasks
    
    def assignAndWork(self, advertisements, ids):
        self.assign(advertisements, ids)
        return self.work()
    
    def getUtilRate(self):
        totalWorkTime = 0
        totalWorkCount = 0
        for moderator in self.moderators:
            totalWorkTime += moderator.totalWorkTime
            totalWorkCount += moderator.workcount
        return totalWorkCount / totalWorkTime
    
class MockModeratorBuilder:
    def build(self):
       ans = ""
       for i in range(0, 9):
           value = random.randint(5, 20)
           ans += str(value) + "/"
       ans += str(random.randint(5, 20))
       return ans
    
    def read(self, string):
       strings = string.split("/")
       ability = []
       for i in range(0, len(strings)):
          ability.append(int(strings[i]))
       return MockModerator(ability)

class Moderator:
    def __init__(self, Properties, estimator):
         self.Properties = Properties
         self.workOn = None
         self.expectedRemainingTime = 0
         self.workcount = 0
         self.totalWorkTime = 0
         self.estimator = estimator
        
    def isIdle(self):
        return self.workOn == None
    
    def assign(self, advertisement):
        if(not self.isIdle()):
            raise Exception("Moderator is not idle")
        self.workOn = advertisement
        self.expectedRemainingTime = self.estimator.estimate(self.Properties, advertisement)
    
    # work; if the task is completed, than add it to the competedTasks list
    def work(self, completedTasks):
        self.totalWorkTime += 1
        if(not self.isIdle()):
          self.expectedRemainingTime -= 1
          self.workcount += 1
          if(self.expectedRemainingTime == 0):
              completedTasks.append(self.workOn)
              self.workOn = None
    
    def getExpectedRemainingTime(self):
        return self.expectedRemainingTime

class ModeratorBuilder:
    def __init__(self, estimator):
        self.estimator = estimator    
       
    def read(self, string):
       properties = {}
       property_strs = string.split("/")
       for i in range(0, len(property_strs)):
          property_str = property_strs[i]
          property = property_str.split(":")
          properties[property[0]] = property[1]
        
       return Moderator(properties, self.estimator)


