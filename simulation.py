import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from managers.AdvertisementManager import *
from managers.ModeratorManager import *

# simulator
def simulate(adManager: AdvertisementManager, modManager: ModeratorManager, allocator):
    while (not adManager.allDone()):
        # start of round n
        adManager.update()

        allocator.allocate(adManager.getUnassignedAds(),
                           modManager.getModerators())

        modManager.work()

    waitLoss = adManager.getLoss()
    inaccuracyLoss = allocator.getInaccuracyLoss()
    loss = waitLoss + inaccuracyLoss
    utilRate = modManager.getUtilRate()
    return loss, utilRate