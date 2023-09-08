class DurationEstimator:
    @staticmethod
    def estimate(mod, ad):
        modTime = mod.properties["handling time"]
        adST = ad.properties["baseline_st"]
        if modTime == 0:
            return adST * 40
        return modTime * adST / 2500