def computePairs(ads, moderators):
    tasks = []
    moderatorIDs = []
    nextModerator = 0
    for ad in ads:
        for i in range(nextModerator, len(moderators)):
            if moderators[i].isIdle():
                tasks.append(ad)
                moderatorIDs.append(i)
                nextModerator = i + 1
                break
        if nextModerator == len(moderators):
            break
    return tasks, moderatorIDs
