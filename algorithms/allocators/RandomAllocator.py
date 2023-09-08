class RandomAllocator:
    def __init__(self, unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator
        self.inaccuracyLoss = 0

    def allocate(self, ads, mods):
        mods = list(filter(lambda mod: mod.isIdle(), mods))
        while (0 < len(ads) and 0 < len(mods)):
            ad = ads.pop()
            mod = mods.pop()
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
