class GreedyAllocator:
    def __init__(self, unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator

    def allocate(self, ads, mods):
        ads.sort(key=lambda ad: ad.value)
        while (0 < len(ads)):
            # most valuable ad
            ad = ads.pop()
            mod = mod = max(mods, key=lambda
                mod: self.unitTimeValueEstimator.estimate(mod, ad))
            mod.assign(ad,
                       self.unitTimeValueEstimator.estimateDuration(mod, ad))


def greedyAllocatorTest():
    class mockMod:
        def __init__(self, value):
            self.value = value
            self.time = 0

        def assign(self, ad, duration):
            self.time += duration
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

    class mockUnitTimeValueEstimator:
        def estimate(self, mod, ad):
            return mod.value / (1 + mod.time)

        def estimateDuration(self, mod, ad):
            return 5

    mod1, mod9 = mockMod(1), mockMod(9)
    ad1, ad2, ad3 = mockAd(1), mockAd(2), mockAd(3)
    allocator = GreedyAllocator(mockUnitTimeValueEstimator())
    allocator.allocate([ad1, ad2, ad3], [mod1, mod9])
    ok = ad3.assigned == mod9 and ad2.assigned == mod9 and ad1.assigned == mod1
    if ok:
        print("GreedyAllocatorTest passed")
    else:
        print("GreedyAllocatorTest failed")
