# This allocator tries to give the best ad to the best mod, but if the mod
# is working and not idle, we wait.
# However, we still pretend that we gave the job to the mod, so that the less
# valuable ads are discouraged from crowding the best mods.
class ModelBasedGreedyAllocator:
    def __init__(self, unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator
        self.inaccuracyLoss = 0

    def allocate(self, ads, mods):
        # keeps track of "pretending to give jobs"
        plannedQueueingAdsDurationPerMod = {}
        for mod in mods:
            plannedQueueingAdsDurationPerMod[mod.id] = 0
        
        ads.sort(key=lambda ad: ad.value)
        copyAds = ads.copy()
        while (0 < len(copyAds)):
            # most valuable ad
            ad = copyAds.pop()

            # filter for mod in same market
            matchingMods = [mod for mod in mods if ad.properties["delivery_country"] in mod.properties["market"]]

            # if no suitable moderator, reject ad
            if not matchingMods:
                ad.assign()
                ad.done()
                continue

            # Assign to the moderator with the highest value per unit time even
            # after accounting for the time it takes to finish the current tasks.
            # Time to finish current tasks includes the ads we pretended to give
            mod = max(matchingMods, key=lambda
                mod: self.unitTimeValueEstimator.estimateProfit(mod,ad) / (
                    self.unitTimeValueEstimator.estimateDuration(mod,
                                                                 ad) + mod.totalTaskRemainTime + plannedQueueingAdsDurationPerMod[mod.id]))

            # if most suitable mod is not currently idle, wait for them
            if not mod.isIdle():
                plannedQueueingAdsDurationPerMod[mod.id] += self.unitTimeValueEstimator.estimateDuration(mod, ad)
                continue
            else:
                # if most suitable mod is idle, give to them
                ads.remove(ad)
                mod.assign(ad, self.unitTimeValueEstimator.estimateDuration(mod, ad))
                self.inaccuracyLoss += self.unitTimeValueEstimator.estimateInaccuracyLoss(
                    mod, ad)

    def getInaccuracyLoss(self):
        return self.inaccuracyLoss


def greedyAllocatorTest():
    class mockMod:
        def __init__(self, value):
            self.value = value
            self.totalTaskRemainTime = 0
            self.id = None
            self.properties = {"market": ["US", "CA"]}

        def assign(self, ad, duration):
            self.totalTaskRemainTime += duration
            ad.assignTo(self)
        def isIdle(self):
            return self.totalTaskRemainTime == 0

    class mockAd:
        def __init__(self, value):
            self.value = value
            self.isAssigned = False
            self.assigned = None
            self.properties = {"delivery_country": "US"}

        def assign(self):
            self.isAssigned = True

        def assignTo(self, mod):
            self.assigned = mod

    class mockUnitTimeValueEstimator:
        def estimate(self, mod, ad):
            return (mod.value + ad.value)/2
        def estimateProfit(self, mod, ad):
            return mod.value + ad.value
        def estimateDuration(self, mod, ad):
            return 2
        def estimateInaccuracyLoss(self, mod, ad):
            return 0

    mod2, mod7 = mockMod(2), mockMod(7)
    mods = [mod2, mod7]
    mod2.id = 0
    mod7.id = 1
    ok = True
    ad10, ad2, ad1 = mockAd(10), mockAd(2), mockAd(1)
    allocator = ModelBasedGreedyAllocator(mockUnitTimeValueEstimator())
    allocator.allocate([ad10, ad2, ad1], [mod2, mod7])
    ok = ok and ad10.assigned == mod7 and ad2.assigned == None and ad1.assigned == mod2
    if ok:
        print("GreedyAllocatorTest passed")
    else:
        print("GreedyAllocatorTest failed")
      
greedyAllocatorTest()
