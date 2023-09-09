import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from entities import Advertisement as ad


class AdvertisementManager:
    def __init__(self, advertisementStream):
        self.advertisementStream = advertisementStream
        self.allAds = []
        self.incompletedAds = {}
        self.unAssignedAds = {}
        self.timeRound = 0
        self.nextId = 0
        self.totalLost = 0

    def update(self):

        self.incompletedAds = {k: v for k, v in self.incompletedAds.items() if not v.isDone}

        for ad in self.incompletedAds.values():
            ad.updateLoss()

        self.unAssignedAds = {k: v for k, v in self.unAssignedAds.items() if not v.isAssigned}

        # get new incoming flow of ads
        if self.timeRound < len(self.advertisementStream):
            for ad in self.advertisementStream[self.timeRound]:
                ad.setId(self.nextId)
                self.incompletedAds[self.nextId] = ad
                self.unAssignedAds[self.nextId] = ad
                self.allAds.append(ad)
                self.nextId += 1
        self.timeRound += 1

    def getUnassignedAds(self):
        return list(self.unAssignedAds.values())

    def allDone(self):
        return len(self.incompletedAds) == 0 and self.timeRound > 0

    def getLoss(self):
        totalLoss = 0
        for ad in self.allAds:
            totalLoss += ad.getLoss()
        return totalLoss
    
    def getLossList(self):
        lossList = []
        for ad in self.allAds:
            lossList.append(ad.getLoss())
        return lossList


def AdvertismentManagerTest():
    class mockEstimator:
        def estimate(self, a):
            return 5

        def estimateRisk(self, a):
            return 0.1

        def estimateRevenue(self, a):
            return 6

    ad00 = ad.Advertisement({}, mockEstimator())
    ad01 = ad.Advertisement({}, mockEstimator())
    ad10 = ad.Advertisement({}, mockEstimator())
    ads0 = [ad00, ad01]
    ads1 = [ad10]
    adss = [ads0, ads1]
    adM = AdvertisementManager(adss)
    ok = adM.getUnassignedAds() == []
    adM.update()
    ok = ok and adM.getUnassignedAds() == ads0
    ad00.assign()
    ad00.done()
    ad01.assign()
    adM.update()
    ok = ad00.accumulatedLoss == 0 and adM.getUnassignedAds() == ads1 and ad01.accumulatedLoss == 5
    ad01.done()
    ad10.assign()
    adM.update()

    ok = ok and adM.getUnassignedAds() == [] and ad10.accumulatedLoss == 5 and adM.getLoss() == 10
    if ok:
        print("AdvertismentManagerTest passed")
    else:
        print("AdvertismentManagerTest failed")


# AdvertismentManagerTest()
