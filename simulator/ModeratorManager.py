class Moderator:

    def __init__(self, ability):
         Ability = ability
         workOn = None
         expectedRemainingTime = 0
        
    

    def getAdTimeEstimate(self, advertisement):
        return self.Ability[advertisement.type]
    
    def isIdle(self):
        return self.workOn == None
    
    def assign(self, advertisement):
        if(not self.isIdle()):
            raise Exception("Moderator is not idle")
        workOn = advertisement
        expectedRemainingTime = self.getAdTimeEstimate(advertisement)

    def work(self):
        if(not self.isIdle()):
          expectedRemainingTime -= 1
          if(expectedRemainingTime == 0):
            workOn = None

class ModeratorManager:
    moderators = []
    
    def getInstance():
        return moderatorManager
    
    def getModerator():
       return moderators

    def assign(id, advertisement):
        moderators[id].assign(advertisement)
        
    def work():
        for moderator in this.moderators:
            moderator.work()
    
    
