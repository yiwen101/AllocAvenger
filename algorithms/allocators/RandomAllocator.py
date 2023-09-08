class RandomAllocator:
    def __init__(self, unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator
        self.inaccuracyLoss = 0

    def allocate(self, ads, mods):
        copyAds = ads.copy()
        while (0 < len(copyAds) and 0 < len(mods)):
            ad = copyAds.pop()
            # filter for market
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

            # if no idle and matching mod, wait
            if not matchingMods:
                continue

            mod = matchingMods.pop()
            ads.remove(ad)
            mod.assign(ad, self.unitTimeValueEstimator.estimateDuration(mod, ad))
            self.inaccuracyLoss += self.unitTimeValueEstimator.estimateInaccuracyLoss(
                mod, ad)

    def getInaccuracyLoss(self):
        return self.inaccuracyLoss


def randomAllocatorTest():
    class mockMod:
        def __init__(self, value):
            self.idle = True
            self.value = value
            self.assigned = None

        def isIdle(self):
            return self.idle

        def assign(self, ad):
            self.idle = False
            ad.assign()
            ad.assignTo(self)

    class mockAd:
        def __init__(self, value):
            self.value = value
            self.isAssigned = False
            self.assigned = None

        def assign(self):
            self.isAssigned = True

        def assignTo(self, mod):
            self.assigned = mod

    ad3, ad1, ad2, ad4 = mockAd(3), mockAd(1), mockAd(3), mockAd(4)
    mod1, mod2, mod3 = mockMod(3), mockMod(1), mockMod(2)

    allocator = RandomAllocator(None)
    allocator.allocate([ad3, ad1, ad2, ad4], [mod1, mod2, mod3])
    ok = not mod1.isIdle() and not mod2.isIdle() and not mod3.isIdle() and ad1.isAssigned and ad2.isAssigned and not ad3.isAssigned and ad4.isAssigned
    if ok:
        print("RandomAllocatorTest passed")
    else:
        print("RandomAllocatorTest failed")
