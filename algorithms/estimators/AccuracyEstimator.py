class AccuracyEstimator:
    @staticmethod
    def estimate(mod, ad):
        modAcc = mod.properties["accuracy"]
        return modAcc