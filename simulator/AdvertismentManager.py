import random



def generateAndWriteAdvertisment():
    advertisements = []
    for i in range(0, 10):
        advertisements.append(Advertisment())
    fs.write(advertisements)
    




class Advertisment:
    def __init__(self, value, adType):
        self.value = value
        self.adType = adType




    
    

class AdvertismentManager:
    
   

    def get_advertisments():
        advertisements = []
        for _, value in current_advertisments.items():
            advertisements.append(value)
        
        return advertisements
    
    def markAsDone(id):
        current_advertisments.pop(id)
    
    def AllDone():
        return len(current_advertisments) == 0

