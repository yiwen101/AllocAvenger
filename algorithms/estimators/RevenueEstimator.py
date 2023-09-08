class RevenueEstimator:
    @staticmethod
    def estimate(ad):
        avgAdRev = ad.properties["avg_ad_revenue"]
        return avgAdRev