# This allocator gives the most valuable ad to best matching mod, even if
# the mod is not idle.
class GreedyAllocator:
    def __init__(self, unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator
        self.inaccuracyLoss = 0

    def allocate(self, ads, mods):
        ads.sort(key=lambda ad: ad.value)
        while (0 < len(ads)):
            # most valuable ad
            ad = ads.pop()

            # filter for mod in same market
            matchingMods = [mod for mod in mods if ad.properties["delivery_country"] in mod.properties["market"]]

            # if no suitable moderator, reject ad
            if not matchingMods:
                ad.assign()
                ad.done()
                continue

            # assign to the moderator with the highest value per unit time even after accounting for the time it takes to finish the current tasks
            mod = max(matchingMods, key=lambda
                mod: self.unitTimeValueEstimator.estimateProfit(mod, ad) / (
                    self.unitTimeValueEstimator.estimateDuration(mod,
                                                                 ad) + mod.totalTaskRemainTime))

            # it could be that this mod already has too many ads that the mod has used up
            # their total work time, so we try until we can successfully assign
            successfulAssignment = False
            while not successfulAssignment:
                # if no possible assignment, reject ad
                if not matchingMods:
                    ad.assign()
                    ad.done()
                    break
                mod = max(matchingMods, key=lambda
                    mod: self.unitTimeValueEstimator.estimateProfit(mod, ad) / (
                        self.unitTimeValueEstimator.estimateDuration(mod,
                                                                     ad) + mod.totalTaskRemainTime))
                # try giving to the next best mod
                successfulAssignment = mod.assign(ad,
                           self.unitTimeValueEstimator.estimateDuration(mod, ad))
                matchingMods.remove(mod)

            # if assigned, update loss
            if successfulAssignment:
                self.inaccuracyLoss += self.unitTimeValueEstimator.estimateInaccuracyLoss(mod, ad)

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
            return True
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

    mod1, mod9 = mockMod(1), mockMod(8)
    ad1, ad2, ad3, ad4, ad5 = mockAd(0), mockAd(2), mockAd(3),mockAd(4), mockAd(5)
    allocator = GreedyAllocator(mockUnitTimeValueEstimator())
    allocator.allocate([ad1, ad2, ad3, ad4,ad5], [mod1, mod9])
    # 13/2 vs 6/2; 12/4 vs 5/2; 11/6 vs 4/2; 10/6 vs 3/4; 9/8 vs 2/2
    ok = ad3.assigned == mod1 and ad2.assigned == mod9 and ad1.assigned == mod9 and ad4.assigned == mod9 and ad5.assigned == mod9
    if ok:
        print("GreedyAllocatorTest passed")
    else:
        print("GreedyAllocatorTest failed")

# greedyAllocatorTest()