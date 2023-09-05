def readAdvertisementStream(builder, fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
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

# each line ends with \n should represents one moderator
def readModerators(builder, fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
        Moderators = []
        for i in range(0, len(lines)):
            Moderators.append(builder.read(lines[i].replace("\n", "")))
    file.close()
    return Moderators  

