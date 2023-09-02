from data import adManager, modManager


''''
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
'''

'''
builder = mockAdvertisementBuilder()
advertisementss = readAdvertisementStream(builder, "./inputs/AdvertisementStream.txt")
print(advertisementss)
'''
print(adManager)

    
    
    