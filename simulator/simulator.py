
from Simulator.AdvertismentManager import AdvertismentManager
from Simulator.ModeratorManager import ModeratorManager

# init, read moderators and advertisements from file



def simulate(advertisementStream, moderators, algo):
    timeround = 0
    moderatorManager = ModeratorManager(moderators)
    advertisementManager = AdvertismentManager(advertisementStream)
    database = database()
    drawer = drawer()
    
    while(not advertisementManager.isDone()):
        timeRound += 1
        advertisementManager.getNewAdvertisements()
        advertisements = advertisementManager.getAdvertisement()

        moderators = moderatorManager.getModerators()
        pairs = algo(advertisements, moderators)
        moderatorManager.assign(pairs)
        finishedTasks = moderatorManager.work()
        advertisementManager.markAsDone(finishedTasks)

    drawer.draw(database)


    
    
    