# This allocator gives the best ad to the best, currently idle mod.
class GreedyIdleOnlyAllocator:
    def __init__(self, unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator
        self.inaccuracyLoss = 0

    def allocate(self, ads, mods):
        ads.sort(key=lambda ad: ad.value)
        copyAds = ads.copy()
        while (0 < len(copyAds) and 0 < len(mods)):
            # most valuable ad
            ad = copyAds.pop()
            # filter for mod with same market
            matchingMods = [mod for mod in mods if
                            ad.properties["delivery_country"] in mod.properties[
                                "market"]]

            # if no working and matching mod, reject ad
            if not matchingMods:
                ad.assign()
                ad.done()
                ads.remove(ad)
                continue

            matchingMods = [mod for mod in matchingMods if mod.isIdle()]

            # if no matching mod is idle, wait till next round
            if not matchingMods:
                continue

            # otherwise give it to the best matching mod
            mod = max(matchingMods, key=lambda
                mod: self.unitTimeValueEstimator.estimate(mod, ad))
            matchingMods.remove(mod)
            ads.remove(ad)
            mod.assign(ad,
                       self.unitTimeValueEstimator.estimateDuration(mod, ad))
            self.inaccuracyLoss += self.unitTimeValueEstimator.estimateInaccuracyLoss(
                mod, ad)

    def getInaccuracyLoss(self):
        return self.inaccuracyLoss


def greedyIdleOnlyAllocatorTest():
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

    ad1, ad2, ad3 = mockAd(1), mockAd(2), mockAd(3)
    mod1, mod2, mod3 = mockMod(1), mockMod(2), mockMod(3)
    mod2.totalTaskRemainTime = 1
    allocator = GreedyIdleOnlyAllocator(mockUnitTimeValueEstimator())
    allocator.allocate([ad1, ad2, ad3], [mod1, mod2, mod3])
    ok = not mod1.isIdle() and not mod2.isIdle() and not mod3.isIdle()
    ok = ok and ad2.assigned == mod1 and ad3.assigned == mod3
    if ok:
        print("GreedyIdleOnlyAllocatorTest passed")
    else:
        print("GreedyIdleOnlyAllocatorTest failed")

# greedyIdleOnlyAllocatorTest()