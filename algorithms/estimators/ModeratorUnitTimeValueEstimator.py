import Moderator


class ModeratorUnitTimeValueEstimator:
    def __init__(self, durationEstimator, accuracyEstimator, punishingFactor, ):
        self.durationEstimator = durationEstimator
        self.punishingFactor = punishingFactor
        self.accuracyEstimator = accuracyEstimator

    def estimate(self, mod, ad):
        risk = ad.risk
        revenue = ad.revenue
        accuracy = self.accuracyEstimator.estimate(mod, ad)
        duration = self.durationEstimator.estimate(mod, ad)
        # there are four cases, when there is accurate and happy case, accurate and sad case, false negative, false positive.
        # to consider the UnitTimeValue, consider the sum of the expected value of the four cases ajusted with probability of occurance
        accurateAndHappyCase = (1 - risk) * accuracy * revenue
        # accurateAndSadCase =  risk * accuracy * 0 = 0
        # falseNegative = (1 - risk) * (1-accuracy) * 0 = 0
        falsePositive = -1 * risk * (
                1 - accuracy) * revenue * self.punishingFactor
        return (accurateAndHappyCase + falsePositive) / duration

    def estimateDuration(self, mod, ad):
        return self.durationEstimator.estimate(mod, ad)

class naiveAccuracyEstimator:
    def estimate(self, mod, ad):
        return mod.properties["accuracy"]

class naiveDurationEstimator:
    def estimate(self, mod, ad):
        return ad.properties["baseline_st"] * 5
    
def moderatorUnitTimeValueEstimatorTest():
    class mockDurationEstimator:
        def estimate(self, mod, ad):
            return 5

    class mockAccuracyEstimator:
        def estimate(self, mod, ad):
            return 0.9

    class mockAd:
        def __init__(self):
            self.risk = 0.1
            self.revenue = 5

    estimator1 = ModeratorUnitTimeValueEstimator(mockDurationEstimator(),
                                                 mockAccuracyEstimator(), 0)
    ad = mockAd()
    mod = Moderator({})
    ok = abs(estimator1.estimate(mod, ad) - 0.9 * 5 * 0.9 / 5) < 0.000001
    estimator2 = ModeratorUnitTimeValueEstimator(mockDurationEstimator(),
                                                 mockAccuracyEstimator(), 10)
    ok = ok and abs(estimator2.estimate(mod, ad) - (
            0.9 * 5 * 0.9 / 5 - 10 * 0.1 * 0.1 * 5 / 5)) < 0.000001
    if ok:
        print("moderatorUnitTimeValueEstimatorTest passed")
    else:
        print("moderatorUnitTimeValueEstimatorTest failed")
