from data import adManager, modManager
from algo.computePairs import computePairs


def simulate(advertisementStream, moderators, algo):
    
    while(not adManager.isDone()):
        # start of round n
        
        # add incoming ads this rounds to the pool of unfinished ads
        adManager.update()
        # get the an array of unfinished ads
        ads = adManager.getAdvertisements()
        # get an array of moderators that are available
        mods = modManager.getAvailableModerators()
        # generate paris of assigned ads to moderators
        assignedAds, assignedTos = algo(ads, mods)
        # mark the assigned ads as assigned
        adManager.markAsAssigned(assignedAds)
        # actually work on the assigned ads
        finishedTasks = modManager.assignAndWork(assignedAds, assignedTos)
        # mark the finished ads as done
        adManager.markAsDone(finishedTasks) 
        # end of round n
        adManager.updateLoss()
    
    loss = adManager.getLoss()
    utilRate = modManager.getUtilRate()
    return loss, utilRate




    
    
    