from entities import Advertisement as ad


class RevenueRiskBasedValueEstimator:
    def __init__(self, revenueEstimator, riskEstimator, punishingFactor):
        self.revenueEstimator = revenueEstimator
        self.riskEstimator = riskEstimator
        self.punishingFactor = punishingFactor

    def estimate(self, ad):
        # set the revenue factor of ad to revenue
        revenue = self.revenueEstimator.estimate(ad)
        risk = self.riskEstimator.estimate(ad)
        return (1 - risk) * revenue

    def estimateRevenue(self, ad):
        return self.revenueEstimator.estimate(ad)

    def estimateRisk(self, ad):
        return self.riskEstimator.estimate(ad)

def revenueRiskBasedValueEstimatorTest():
    class mockRevenueEstimator:
        def estimate(self, ad):
            return 5

    class mockRiskEstimator:
        def estimate(self, ad):
            return 0.1

    estimator1 = RevenueRiskBasedValueEstimator(mockRevenueEstimator(),
                                                mockRiskEstimator(), 0)
    ad1 = ad.Advertisement({}, estimator1)
    ok = ad1.risk == 0.1 and ad1.revenue == 5 and ad1.value == 4.5
    estimator2 = RevenueRiskBasedValueEstimator(mockRevenueEstimator(),
                                                mockRiskEstimator(), 10)
    ad2 = ad.Advertisement({}, estimator2)
    ok = ok and ad2.risk == 0.1 and ad2.revenue == 5 and ad2.value == 4.5 - 10 * 0.1 * 5

    if ok:
        print("revenueRiskBasedValueEstimatorTest passed")
    else:
        print("revenueRiskBasedValueEstimatorTest failed")
