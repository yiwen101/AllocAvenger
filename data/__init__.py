
from data.advertisement import AdvertismentManager, MockAdvertisementBuilder
from data.moderator import MockModeratorBuilder, ModeratorManager
from data.reader import readAdvertisementStream, readModerators


adManager = AdvertismentManager(readAdvertisementStream(MockAdvertisementBuilder(), "./inputs/AdvertisementStream.txt"))
modManager = ModeratorManager(readModerators(MockModeratorBuilder(), "./inputs/Moderators.txt"))

print(adManager)
print(modManager)
