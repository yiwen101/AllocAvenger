def computePairs(ads, moderators):
    nextAdID = 0
    tasks = []
    moderatorIDs = []
    for i in range(0, len(moderators)):
        if moderators[i].isIdle() and nextAdID < len(ads):
            tasks.append(ads[nextTaskID])
            moderatorIDs.append(i)
            nextTaskID += 1
    return (moderatorIDs, tasks)    

