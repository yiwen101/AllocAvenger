from raw_parsers import AdvertisementStreamParser as adSPar
from raw_parsers import AdvertisementParser as asPar
from raw_parsers import ModeratorStreamParser as modSPar
from raw_parsers import ModeratorParser as modPar
from managers import AdvertisementManager as adM
from managers import ModeratorManager as modM
# simulator
def simulate(adsFileName, modsFileName, adEstimator, modAdEstimator,
             allocatorClass):
    adStream = adSPar.AdvertisementStreamParser(
        asPar.AdvertisementParser(adEstimator)).parseFile(adsFileName)
    adManager = adM.AdvertisementManager(adStream)

    mods = modSPar.ModeratorStreamParser(modPar.ModeratorParser()).parseFile(modsFileName)
    modManager = modM.ModeratorManager(mods)

    allocator = allocatorClass(modAdEstimator)

    while (not adManager.allDone()):
        # start of round n
        adManager.update()

        allocator.allocate(adManager.getUnassignedAds(),
                           modManager.getModerators())

        modManager.work()

    loss = adManager.getLoss()
    utilRate = modManager.getUtilRate()
    return loss, utilRate