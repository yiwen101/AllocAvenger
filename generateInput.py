# Open a file in write mode (creates the file if it doesn't exist)
import random

from simulator.AdvertismentManager import Advertisment
from simulator.ModeratorManager import Moderator


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


def readAdvertisementStream(builder, fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
        print(lines)
        Advertismentss = []
        for i in range(0, len(lines)):
            current_lines = lines[i].split(" ")
            Advertisments = []
            for j in range(0, len(current_lines)):
                input = current_lines[j]
                if input == "" or input == "\n" or input == " " or input == " \n":
                    continue
                Advertisments.append(builder.read(input))
            Advertismentss.append(Advertisments)
    file.close()
    return Advertismentss

def readModerators(builder, fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
        Moderators = []
        for i in range(0, len(lines)):
            Moderators.append(builder.read(lines[i]))
    file.close()
    return Moderators  
         
class mockAdvertisementBuilder:
    def build(self):
       type = random.randint(0, 10)
       value = random.randint(0, 100)
       return str(type) + "/" + str(value)
    
    def read(self, string):
       strings = string.split("/")
       return Advertisment(int(strings[1]), int(strings[0]))

class mockModeratorBuilder:
    def build(self):
       ans = ""
       for i in range(0, 9):
           value = random.randint(5, 20)
           ans += str(value) + "/"
       ans += str(random.randint(5, 20))
       return ans
    
    def read(self, string):
       strings = string.split("/")
       ability = []
       for i in range(0, len(strings)):
          ability.append(int(strings[i]))
       return Moderator(ability)

'''
builder = mockAdvertisementBuilder()
generateAdvertisementStream(100, 10, builder, "./inputs/AdvertisementStream.txt")
builder = mockModeratorBuilder()
generateModerators(17, builder, "./inputs/Moderators.txt")
'''
stream = readAdvertisementStream(mockAdvertisementBuilder(), "./inputs/AdvertisementStream.txt")
print(stream)