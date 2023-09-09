import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from entities import Moderator as mod


class ModeratorManager:

    def __init__(self, moderators):
        self.moderators = moderators
        self.workingModerators = moderators.copy()

    def getModerators(self):
        return self.workingModerators

    def work(self):
        for moderator in self.workingModerators:
            if not moderator.isWorking:
                self.workingModerators.remove(moderator)
            else:
                moderator.work()

    def getUtilRate(self):
        totalWorkTime = 0
        totalWorkCount = 0
        for moderator in self.moderators:
            totalWorkTime += moderator.totalWorkTime
            totalWorkCount += moderator.effectiveWorkTime
        return totalWorkCount / totalWorkTime
    def getUtilRateList(self):
        utilRateList = []
        for moderator in self.moderators:
            utilRateList.append(moderator.effectiveWorkTime / moderator.totalWorkTime)
        return utilRateList


def ModeratorManagerTest():
    mod1 = mod.Moderator(
        {"moderator": 1, "market": ["US", "CA"], "Productivity": 286.2176,
         "Utilisation": 0.8124, "handling time": 123549, "accuracy": 0.99})
    mod2 = mod.Moderator(
        {"moderator": 2, "market": ["US", "CA"], "Productivity": 286.2176,
         "Utilisation": 0.8124, "handling time": 123549, "accuracy": 0.99})
    mod3 = mod.Moderator(
        {"moderator": 3, "market": ["US", "CA"], "Productivity": 286.2176,
         "Utilisation": 0.8124, "handling time": 123549, "accuracy": 0.99})
    mods = [mod1, mod2, mod3]
    modManager = ModeratorManager([mod1, mod2, mod3])
    ok = modManager.getModerators() == mods
    modManager.work()
    ok = ok and mod1.totalWorkTime == 1 and mod2.totalWorkTime == 1 and mod3.totalWorkTime == 1
    if ok:
        print("ModeratorManagerTest passed")
    else:
        print("ModeratorManagerTest failed")
