import random


class Moderator:

    def __init__(self, ability):
         self.Ability = ability
         self.workOn = None
         self.expectedRemainingTime = 0
         self.workcount = 0
         self.totalWorkTime = 0
        
    

    def getAdTimeEstimate(self, advertisement):
        return self.Ability[advertisement.type]
    
    def isIdle(self):
        return self.workOn == None
    
    def assign(self, advertisement):
        if(not self.isIdle()):
            raise Exception("Moderator is not idle")
        workOn = advertisement
        expectedRemainingTime = self.getAdTimeEstimate(advertisement)

    def work(self, completedTasks):
        self.totalWorkTime += 1
        if(not self.isIdle()):
          expectedRemainingTime -= 1
          self.workcount += 1
          if(expectedRemainingTime == 0):
              completedTasks.append(workOn)
              workOn = None

class ModeratorManager:
    moderators = []
    
    def __init__(self, moderators):
        self.moderators = moderators
    
    def getModerators(self):
       return self.moderators

    def assign(self,ids, advertisements):
        for i in range(0, len(ids)):
            moderator = self.moderators[ids[i]]
            advertisements = advertisements[i]
            moderator.assign(advertisements)
                 
    def work(self):
        completedTasks = []
        for moderator in self.moderators:
            moderator.work(completedTasks)
        return completedTasks
    
    def assignAndWork(self, ids, advertisements):
        self.assign(ids, advertisements)
        return self.work()
    
    def getUntilRate(self):
        totalWorkTime = 0
        totalWorkCount = 0
        for moderator in self.moderators:
            totalWorkTime += moderator.totalWorkTime
            totalWorkCount += moderator.workcount
        return totalWorkTime / totalWorkCount
    
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
       return Moderator(ability)

