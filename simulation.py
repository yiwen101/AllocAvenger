import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from managers.AdvertisementManager import *
from managers.ModeratorManager import *

# simulator
def simulate(adManager: AdvertisementManager, modManager: ModeratorManager, allocator) -> (float, float, int):
    timestep = 0
    while (modManager.getModerators() and not adManager.allDone()):
        # start of round n
        adManager.update()

        allocator.allocate(adManager.getUnassignedAds(),
                           modManager.getModerators())

        modManager.work()
        timestep += 1
        print(timestep)

    waitLoss = adManager.getLoss()
    inaccuracyLoss = allocator.getInaccuracyLoss()
    loss = waitLoss + inaccuracyLoss
    utilRate = modManager.getUtilRate()
    return loss, utilRate, timestep

def simulateExtended(adManager: AdvertisementManager, modManager: ModeratorManager, allocator) -> (float, float, int, list):
    timestep = 0
    while (modManager.getModerators() and not adManager.allDone()):
        # start of round n
        adManager.update()

        allocator.allocate(adManager.getUnassignedAds(),
                           modManager.getModerators())

        modManager.work()
        timestep += 1
        print(timestep)

    waitLoss = adManager.getLoss()
    inaccuracyLoss = allocator.getInaccuracyLoss()
    loss = waitLoss + inaccuracyLoss
    utilRate = modManager.getUtilRate()
    utilRateList = modManager.getUtilRateList()
    return loss, utilRate, timestep, utilRateList