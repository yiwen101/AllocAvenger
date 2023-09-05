#data/moderator
class Moderator:
    def __init__(self, Properties):
         self.Properties = Properties
         self.tasks = []
         self.tasksEstimatedTime = []
         self.totalTaskRemainTime = 0
         self.effectiveWorkTime = 0
         self.totalWorkTime = 0
        
    def isIdle(self):
        return len(self.tasks) == 0
    
    def assign(self, advertisement, estimatedTime):
        advertisement.assign()
        self.tasks.append(advertisement)
        self.tasksEstimatedTime.append(estimatedTime)
        self.totalTaskRemainTime += estimatedTime
    
    # sideeffect: if the task is completed, than add it to the competedTasks list
    def work(self):
        self.totalWorkTime += 1
        if(not self.isIdle()):
            self.effectiveWorkTime += 1
            self.tasksEstimatedTime[0] -= 1
            self.totalTaskRemainTime -= 1
            if(self.tasksEstimatedTime[0] == 0):
                self.tasks.pop(0).done()
                self.tasksEstimatedTime.pop(0)
                
def ModeratorTest():
    class fakeAd:
        def __init__(self):
            self.isDone = False
            self.isAssigned = False
        def assign(self):
            self.isAssigned = True
        def done(self):
            self.isDone = True
    
    md = Moderator({"moderator":1,"market":["US","CA"],"Productivity":286.2176,"Utilisation":0.8124,"handling time":123549,"accuracy":0.99})
    ok = md.isIdle() and md.totalTaskRemainTime == 0 
    ad1, ad2, ad3 = fakeAd(), fakeAd(), fakeAd()
    ok = not ad1.isAssigned
    md.assign(ad1, 2)
    ok = ok and not md.isIdle() and md.totalTaskRemainTime == 2 and ad1.isAssigned and not ad1.isDone
    md.work()
    ok = ok and not md.isIdle() and md.totalTaskRemainTime == 1 and not ad1.isDone
    md.work()
    ok = ok and md.isIdle() and md.totalTaskRemainTime == 0 and ad1.isDone
    md.work()
    ok = ok and md.effectiveWorkTime == 2 and md.totalWorkTime == 3
    md.assign(ad2, 2)
    md.assign(ad3, 1)
    md.work()
    ok = ok and md.totalTaskRemainTime == 2 and ad2.isAssigned and ad3.isAssigned
    md.work()
    ok = ok and md.totalTaskRemainTime == 1 and ad2.isDone
    if ok:
        print("ModeratorTest passed")
    else:
        print("ModeratorTest failed")

class ModeratorManager:
    moderators = []
    
    def __init__(self, moderators):
        self.moderators = moderators
    
    def getModerators(self):
       return self.moderators
                 
    def work(self):
        completedTasks = []
        for moderator in self.moderators:
            moderator.work(completedTasks)
        return completedTasks
    
    def getUtilRate(self):
        totalWorkTime = 0
        totalWorkCount = 0
        for moderator in self.moderators:
            totalWorkTime += moderator.totalWorkTime
            totalWorkCount += moderator.workcount
        return totalWorkCount / totalWorkTime

#data/advertisement
class Advertisement:
    def __init__(self, properties, estimator):
         self.properties = properties
         self.estimator = estimator
         self.accumulatedLoss = 0
         self.isDone = False
         self.isAssigned = False
         self.value = self.estimator.estimate(self)
         self.risk = estimator.estimateRisk(self)
         self.revenue = estimator.estimateRevenue(self)
         
    def assign(self):
        self.isAssigned = True
    
    def done(self):
        self.isDone = True
    
    def updateLoss(self):
        self.accumulatedLoss += self.value
         
    def getLoss(self):
        return self.accumulatedLoss

def AdvertisementTest():
    class mockEstimator:
        def estimate(self,a):
            return 5
        def estimateRisk(self,a):
            return 0.1
        def estimateRevenue(self,a):
            return 6
    
    ad = Advertisement({"ad_id":1747578422390810,"delivery_country":"US","queue_market":["US","CA"],"punish_num":1,"avg_ad_revenue":4796.25,"ad_revenue":513217,"start_time":"10/24/2022 14:36","baseline_st":1.78}, mockEstimator())
    ok = not ad.isDone and not ad.isAssigned and ad.getLoss() == 0
    ad.assign()
    ok = ok and ad.isAssigned
    ad.updateLoss()
    ok = ok and ad.getLoss() == 5
    ad.done()
    ok = ok and ad.isDone
    if ok:
        print("AdvertisementTest passed")
    else:
        print("AdvertisementTest failed")

class AdvertismentManager:
    def __init__(self, advertisementStream):
        self.advertisementStream = advertisementStream
        self.allAds = []
        self.incompletedAds = {}
        self.unAssignedAds = {}
        self.timeRound = 0
        self.nextId = 0
        self.totalLost = 0
    
    def update(self):
        for ad in self.incompletedAds.values():
            if ad.isdone:
                self.incompletedAds.pop(ad.getID())
            else:
                ad.updateLoss()
        
        for ad in self.unAssignedAds.values():
            if ad.isAssigned:
                self.unAssignedAds.pop(ad.getID())
                
        # get new incoming flow of ads
        if self.timeRound < len(self.advertisementStream):
            for ad in self.advertisementStream[self.timeRound]:
                ad.setID(self.nextId)
                self.incompletedAds[self.nextId] = ad
                self.unAssignedAds[self.nextId] = ad
                self.allAds.append(ad)
                self.nextId += 1
        self.timeRound += 1
            
    def getUnassignedAds(self):
        return self.unAssignedAds.values() 
    
    def allDone(self):
        return len(self.incompletedAds) == 0 and self.timeRound > 0
    
    def getLoss(self):
        totalLoss = 0
        for ad in self.allAds:
            totalLoss += ad.getLoss()
        return totalLoss
            

# Parser
def propertyAssertHelper(v1, v2,property):
    for i in range (0,len(v1)):
       if not property[v1[i]] == v2[i]:
           print("for " + v1[i], "expect " + v2[i]+", but get " + property[v1[i]])
           return False
    return True         

class strToPropertiesParser: 
    def parse(self,string):
        properties = {}
        property_strs = string.split("::")
        for i in range(0, len(property_strs)):
          property_str = property_strs[i]
          property = property_str.split("//")
          properties[property[0]] = property[1]
        return properties

def strToPropertiesParserTest():
    parser = strToPropertiesParser()
    testStr = "p1//v1::p2//v2::p3//v3"
    property = parser.parse(testStr)
    ok = propertyAssertHelper(["p1","p2","p3"], ["v1","v2","v3"],property)
    if ok:
        print("strToPropertiesParserTest passed")
        return True
    else:
        print("strToPropertiesParserTest failed")
        return False

class adPropertiesParser:
    def __init__(self):
        self.baseParser = strToPropertiesParser()
    
    # todo p_data//20230807, start_time//10/24/2022 14:36, last_pushnish_begin_date are left as string; 
    def parse(self, advertisementStr):
        properties = self.baseParser.parse(advertisementStr)
        # In Python 3, the int type can represent integers of practically unlimited size, so there's usually no need to worry about the limitations of fixed-size integer types as you would in some other programming languages
        properties["ad_id"]=int(properties["ad_id"])
        properties["queue_market"] = properties["queue_market"].split("&")
        properties["punish_num"]=int(properties["punish_num"])
        properties["avg_ad_revenue"] = float(properties["avg_ad_revenue"])
        properties["ad_revenue"] = int(properties["ad_revenue"])
        properties["baseline_st"] = float(properties["baseline_st"])
        return properties

def adPropertiesParserTest():
    parser = adPropertiesParser()
    testStr = "p_data//20230807::ad_id//1747578422390810::delivery_country//US::queue_market//US&CA::punish_num//1::avg_ad_revenue//4796.25::ad_revenue//513217::start_time//10/24/2022 14:36::baseline_st//1.78"
    property = parser.parse(testStr)
    ok = propertyAssertHelper(["ad_id","queue_market","punish_num","avg_ad_revenue","ad_revenue","baseline_st"],[1747578422390810,["US","CA"],1,4796.25,513217,1.78],property)
    if ok:
        print("adPropertiesParserTest passed")
    else:
        print("adPropertiesParserTest failed")

class moderatorPropertiesParser:
    def __init__(self):
        self.baseParser = strToPropertiesParser()
    # make sure the data input is valid, entry with empty values are either rewritten as null value of the type or discarded.
    def parse(self,moderatorStr):
        properties = self.baseParser.parse(moderatorStr)
        properties["moderator"] =int(properties["moderator"])
        # this part, the one working on dealing iwth the input data should do extra work
        properties["market"]= properties["market"].split("&")
        # not sure why these two are in capital letters in the doc
        properties["Productivity"] = float(properties["Productivity"])
        properties["Utilisation"] = float(properties["Utilisation"])
        properties["handling time"] = float(properties["handling time"])
        properties["accuracy"] = float(properties["accuracy"])
        return properties

def moderatorPropertiesParserTest():
    parser = moderatorPropertiesParser()
    testStr = "moderator//1689841547143170::market//SA&OM&BH&QA&JO::Productivity//286.2176::Utilisation//0.8124::handling time//123549::accuracy//0.99"
    property = parser.parse(testStr)
    ok = propertyAssertHelper(["moderator","market","Productivity","Utilisation","handling time","accuracy"],[1689841547143170,["SA","OM","BH","QA","JO"],286.2176,0.8124,123549,0.99],property)
    if ok:
        print("moderatorPropertiesParserTest passed")
    else:
        print("moderatorPropertiesParserTest failed")

class advertisementParser:
    def __init__(self, estimator):
        self.propertiesParser = adPropertiesParser()
        self.estimator = estimator
        
    def parse(self,advertisementStr):
        properties = self.propertiesParser.parse(advertisementStr)
        return Advertisement(properties, self.estimator)
    
class moderatorParser:
    def __init__(self, estimator):
        self.propertiesParser = moderatorPropertiesParser()
        self.estimator = estimator
        
    def parse(self,moderatorStr):
        properties = moderatorPropertiesParser.parse(moderatorStr)
        return Moderator(properties, self.estimator)

class advertisementStreamParser:
    def __init__(self, advertisementParser):
        self.advertisementParser = advertisementParser
    
    def parseFile(self, fileName):
        with open(fileName, "r") as file:
            lines = file.readlines()
            Advertismentss = []
            for i in range(0, len(lines)):
                Advertisments = self.parseAds(lines[i])
                Advertismentss.append(Advertisments)
            
            file.close()
            return Advertismentss
     
    def parseAds(self,adsStr):
        Advertisments = []
        adsStr = adsStr.split("ADEND!")
        for i in range(0, len(adsStr)):
            input = adsStr[i]
            if input == "" or input == "\n" or input == " " or input == " \n":
                continue
            Advertisments.append(self.advertisementParser.parse(input.strip()))
        return Advertisments

def advertisementStreamParserTest():
    class moveAdPArser:
        def parse(self, adStr):
            return adStr
    parser = advertisementStreamParser(moveAdPArser())
    adss = parser.parseFile("inputs/adStreamParserTest.txt")
    ok = len(adss) == 2 and len(adss[1]) == 3 and adss[0][0]=="ad1" and adss[1][2]=="ad6"
    if ok:
        print("advertisementStreamParserTest passed")
    else:
        print("advertisementStreamParserTest failed")

class moderatorsParser:
    def __init__(self, moderatorParser):
        self.moderatorParser = moderatorParser
    
    def parseFile(self, fileName):
        with open(fileName, "r") as file:
            # each line is one moderator
            lines = "".join(file.readlines()).strip().split("\n")
            Moderators = []
            for i in range(0, len(lines)): 
                Moderators.append(self.moderatorParser.parse(lines[i]))
        file.close()
        return Moderators  

def moderatorParserTest():
    class moveAdPArser:
        def parse(self, adStr):
            return adStr
    parser = moderatorsParser(moveAdPArser())
    mds = parser.parseFile("inputs/moderatorsParserTest.txt")
    ok = len(mds) == 2 and mds[0]=="md1" and mds[1] == "md2"
    if ok:
        print("moderatorParserTest passed")
    else:
        print("moderatorParserTest failed")
# algorithm

class revenueRiskBasedValueEstimator:
    def __init__(self, revenueEstimator, riskEstimator, punishingFactor):
        self.revenueEstimator = revenueEstimator
        self.riskEstimator = riskEstimator
        self.punishingFactor = punishingFactor
    def estimate(self, ad):
        # set the revenue factor of ad to revenue
        revenue = self.revenueEstimator.estimate(ad)
        risk = self.riskEstimator.estimate(ad)
        return (1 - risk) * revenue - risk * revenue * self.punishingFactor
    def estimateRevenue(self, ad):
        return self.revenueEstimator.estimate(ad)
    def estimateRisk(self, ad):
        return self.riskEstimator.estimate(ad)
 
class moderatorUnitTimeValueEstimator:
    def __init__(self, durationEstimator, punishingFactor, accuracyEstimator):
        self.durationEstimator = durationEstimator
        self.punishingFactor = punishingFactor
        self.accuracyEstimator = accuracyEstimator
    def estimate(self, mod, ad):
        risk = ad.risk
        revenue = ad.revenue
        accuracy = self.accuracyEstimator.estimate(mod, ad)
        duration = self.durationEstimator.estimate(mod, ad)
        # there are four cases, when there is accurate and happy case, accurate and sad case, false negative, false positive.
        # to consider the UnitTimeValue, consider the sum of the expected value of the four cases ajusted with probability of occurance
        accurateAndHappyCase = (1 - risk) * accuracy * revenue
        # accurateAndSadCase =  risk * accuracy * 0 = 0
        # falseNegative = (1 - risk) * (1-accuracy) * 0 = 0
        falsePositive = -1 * risk * (1-accuracy) * revenue * self.punishingFactor
        return (accurateAndHappyCase + falsePositive) / duration
    
    def estimateDuration(self, mod, ad):
        return self.durationEstimator.estimate(mod, ad)

class greedyIdleOnlyAllcator:
    def __init__(self,unitTimeValueEstimator):
        self.unitTimeValueEstimator = unitTimeValueEstimator
    
    def allocate(self, ads, mods):
        tasks = []
        moderatorIDs = []
        mods = mods.filter(lambda mod: mod.isIdle())
        ads = ads.sort(key=lambda ad: ad.value)
        
        while(0 < len(ads)):
            #most valuable ad
            ad = ads.pop()
            mod = mods.max(key=lambda mod: self.unitTimeValueEstimator.estimate(mod, ad))
            tasks.append(ad)
            moderatorIDs.append(mod.getID())
        
        return tasks, moderatorIDs          
 
class randomAllcator:
    def allocate(self, ads, mods):
        tasks = []
        moderatorIDs = []
        nextAd = 0
        ads = ads.sort(key=lambda ad: ad.value)
        
        while(0 < len(ads) and 0 < len(mods)):
            #most valuable ad
            ad = ads.pop()
            mod = mods.pop()
            tasks.append(ad)
            moderatorIDs.append(mod.getID())      
        return tasks, moderatorIDs

class greedyAllcator:
    def allocate(self,ads, mods):
        tasks = []
        moderatorIDs = []
        ads = ads.sort(key=lambda ad: ad.value)
        while(0 < len(ads) and 0 < len(mods)):
            #most valuable ad
            ad = ads.pop()
            mod = mods.max(key=lambda mod: mod.unitTimeValueforAd(ad))
            mods.remove(mod)
            tasks.append(ad)
            moderatorIDs.append(mod.getID())
        

       
# simulator
def simulate(adManager, modManager,algo):
    
    while(not adManager.allDone()):
        # start of round n
        
        # add incoming ads this rounds to the pool of unfinished ads
        adManager.update()
        # get the an array of unfinished ads
        ads = adManager.getUnassignedAds()
        # get an array of moderators that are available
        mods = modManager.getModerators()
        # generate paris of assigned ads to moderators
        assignedAds, assignedMods = algo(ads, mods)
        # mark the assigned ads as assigned
        adManager.markAsAssigned(assignedAds)
        # actually work on the assigned ads
        finishedTasks = modManager.assignAndWork(assignedAds, assignedMods)
        # mark the finished ads as done
        adManager.markAsDone(finishedTasks) 
        # end of round n
        adManager.updateLoss()
    
    loss = adManager.getLoss()
    utilRate = modManager.getUtilRate()
    return loss, utilRate

def simulatorTest():
    class mockAdValueEstimator:
        def estimate(self, ad):
            return ad.properties["value"]
    class mockModEstimator:
        def estimate(self,mod,ad):
            return mod.properties["time"]
   
    ad1 = Advertisement()
    return None



# testing
ModeratorTest()
AdvertisementTest()
strToPropertiesParserTest()
adPropertiesParserTest()
moderatorPropertiesParserTest()
advertisementStreamParserTest()
moderatorParserTest()
