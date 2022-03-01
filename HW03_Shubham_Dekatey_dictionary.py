import logger as log
def filter5letterWord(len):
    log.writeLog("Loading Words.txt")
    allWordList = open('words.txt').read().split()
    lenWordList = []
    for i in allWordList:
        if len(i) == len:
            lenWordList.append(i)
    log.writeLog("Creating filterWords.txt")
    with open('filterWords.txt', 'w') as f:
        for item in lenWordList:
            f.write("%s\n" % item)
    log.writeLog("filterWords.txt Created")


def getWordfromFile():
    import random
    my_word = ""
    # my_word = random.choice(open('words.txt').read().split()).strip()
    # print(my_word)
    # return(my_word)
    # allWordList = open('words.txt').read().split()
    # lenWordList = []
    # for i in allWordList:
    #     if len(i) == 5:
    #         lenWordList.append(i)
    log.writeLog("Loading filterWords.txt")
    lenWordList = open('filterWords.txt').read().split()
    my_word = random.choice(lenWordList)
    return my_word

def checkWordExists(guessword):
    # allWordList = open('words.txt').read().split()
    # lenWordList = []
    # for i in allWordList:
    #     if len(i) == 5:
    #         lenWordList.append(i)
    log.writeLog("Loading filterWords.txt")
    lenWordList = open('filterWords.txt').read().split()
    if guessword in lenWordList:
        return 0
    else:
        return 1