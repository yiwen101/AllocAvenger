import numpy as np
class RiskEstimator:
    @staticmethod
    def estimate(ad):
        punishNum = ad.properties["punish_num"]
        if np.isnan(punishNum):
            punishNum = 0
        if punishNum <= 2:
            return 0.12 - 0.03 * punishNum
        return min(0.05 * punishNum - 0.04, 0.6)