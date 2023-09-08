class Advertisement:
    def __init__(self, properties, estimator):
        self.properties = properties
        self.estimator = estimator
        self.accumulatedLoss = 0
        self.isDone = False
        self.isAssigned = False
        self.value = self.estimator.estimate(self)
        self.risk = estimator.estimateRisk(self)
        self.revenue = estimator.estimateRevenue(self)

    def assign(self):
        self.isAssigned = True

    def done(self):
        self.isDone = True

    def updateLoss(self):
        self.accumulatedLoss += self.value / 3000

    def getLoss(self):
        return self.accumulatedLoss

    def setId(self, id):
        self.id = id


def AdvertisementTest():
    class mockEstimator:
        def estimate(self, a):
            return 5

        def estimateRisk(self, a):
            return 0.1

        def estimateRevenue(self, a):
            return 6

    ad = Advertisement({"ad_id": 1747578422390810, "delivery_country": "US",
                        "queue_market": ["US", "CA"], "punish_num": 1,
                        "avg_ad_revenue": 4796.25, "ad_revenue": 513217,
                        "start_time": "10/24/2022 14:36", "baseline_st": 1.78},
                       mockEstimator())
    ok = not ad.isDone and not ad.isAssigned and ad.getLoss() == 0
    ad.assign()
    ok = ok and ad.isAssigned
    ad.updateLoss()
    ok = ok and ad.getLoss() == 5
    ad.done()
    ok = ok and ad.isDone
    if ok:
        print("AdvertisementTest passed")
    else:
        print("AdvertisementTest failed")
