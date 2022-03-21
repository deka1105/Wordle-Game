
from logger import LogX as log
class DictionaryX:

#import logger as log
    def filter5letterWord(wordLen):
        try:
            log.writeLog("Loading Words.txt")
            allWordList = open('words.txt').read().split()
            lenWordList = []
            for i in allWordList:
                if len(i) == wordLen:
                    lenWordList.append(i)
            log.writeLog("Creating filterWords.txt")
        except:
            print("words.txt Loading error")
            log.writeLog("words.txt Loading error")
        # with open('filterWords.txt', 'w') as f:
        #     for item in lenWordList:
        #         f.write("%s\n" % item)
        try:
            with open("filterWords.txt", "w") as outfile:
                outfile.write("\n".join(str(item) for item in lenWordList))
            log.writeLog("filterWords.txt Created")
            return len(lenWordList)
        except:
            return 0
            print("filterWords.txt creation error")
            log.writeLog("filterWords.txt creation error")


    lenWordList = []    

    def __init__(self):
        wordLen = 5
        try:
            log.writeLog("Loading Words.txt")
            allWordList = open('words.txt').read().split()
            lenWordList = []
            for i in allWordList:
                if len(i) == wordLen:
                    lenWordList.append(i)
            log.writeLog("Creating filterWords.txt")
        except:
            print("words.txt Loading error")
            log.writeLog("words.txt Loading error")
        # with open('filterWords.txt', 'w') as f:
        #     for item in lenWordList:
        #         f.write("%s\n" % item)
        try:
            with open("filterWords.txt", "w") as outfile:
                outfile.write("\n".join(str(item) for item in lenWordList))
            log.writeLog("filterWords.txt Created")
            return len(lenWordList)
        except:
            print("filterWords.txt creation error")
            log.writeLog("filterWords.txt creation error")

    def __str__(self) -> str:
        return f"Dictionary(filteredList:{str(self.lenWordList)})"

    def filter5letterWord(wordLen):
        try:
            log.writeLog("Loading Words.txt")
            allWordList = open('words.txt').read().split()
            lenWordList = []
            for i in allWordList:
                if len(i) == wordLen:
                    lenWordList.append(i)
            log.writeLog("Creating filterWords.txt")
        except:
            print("words.txt Loading error")
            log.writeLog("words.txt Loading error")
        # with open('filterWords.txt', 'w') as f:
        #     for item in lenWordList:
        #         f.write("%s\n" % item)
        try:
            with open("filterWords.txt", "w") as outfile:
                outfile.write("\n".join(str(item) for item in lenWordList))
            log.writeLog("filterWords.txt Created")
            return len(lenWordList)
        except:
            print("filterWords.txt creation error")
            log.writeLog("filterWords.txt creation error")

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
        try:
            log.writeLog("Loading filterWords.txt")
            lenWordList = open('filterWords.txt').read().split()
        except:
            print("filterWords.txt Loading error")
            log.writeLog("filterWords.txt Loading error")
        my_word = random.choice(lenWordList)
        return my_word

    def checkWordExists(guessword):
        # allWordList = open('words.txt').read().split()
        # lenWordList = []
        # for i in allWordList:
        #     if len(i) == 5:
        #         lenWordList.append(i)
        try:
            log.writeLog("Loading filterWords.txt")
            lenWordList = open('filterWords.txt').read().split()
        except:
            print("filterWords.txt Loading error")
            log.writeLog("filterWords.txt Loading error")
        if guessword in lenWordList:
            return 0
        else:
            return 1