# Open a file in write mode (creates the file if it doesn't exist)
import random

from data.advertisement import Advertisment,mockAdvertisementBuilder
from data.moderator import Moderator,mockModeratorBuilder


def generateAdvertisementStream(timeRound, maxNumPerRound, builder, fileName):
    with open(fileName, "w") as file:
      for i in range(0, timeRound):
        num = random.randint(0, maxNumPerRound)
        str = ""
        for j in range(0, num):
            str += builder.build() + " "
        file.write(str + "\n")
    file.close()

def generateModerators(number,builder, fileName):
    with open(fileName, "w") as file:
        for i in range(0, number):
            file.write(builder.build() + "\n")
    file.close()



         



'''
builder = mockAdvertisementBuilder()
generateAdvertisementStream(100, 10, builder, "./inputs/AdvertisementStream.txt")
builder = mockModeratorBuilder()
generateModerators(17, builder, "./inputs/Moderators.txt")
'''
