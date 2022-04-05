from glob import glob
from unittest import result
from HW03_Shubham_Dekatey_ui import UiX as ui
from HW03_Shubham_Dekatey_wordle import WordleX as wordle
from HW03_Shubham_Dekatey_dictionary import DictionaryX as dictionary
from tipsHelper import TipsHX
import pandas as pd
import re

class SolverX:

    csvWordList = []
    correctWord = ""

    def __init__(cWord):
         #read csv
        global csvWordList
        global correctWord
        correctWord = cWord

        try:
            data = pd.read_csv("wordRank.csv")
            csvWordList = data['word'].tolist()
        except:
            print("wordRank.csv File Reading error")
    
    def diff(li1, li2):
        return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

    def getCharList(indexList, attemptWord):
        wordList = []
        for i in indexList:
                wordList.append(attemptWord[i])
        return wordList

    def listToWord(ls, words):
        result = []
        for i in ls:
            result.append(words[i])
        return result

    def filterCorrectCharWords(wordList, rIndexList, rCList):
        import pandas as pd
        words = wordList
        df = pd.DataFrame(columns=['1','2','3','4','5'])
        compatibleWords = []

        for w in words:
            chars = [c for c in w]
            print(chars)
            df.loc[len(df)] = chars

        newdf = pd.DataFrame(columns=['1','2','3','4','5'])
        for i in rIndexList:
            charX = rCList[i]
            newdf = df[df[str(i)] == charX]
        
        lsX = newdf.index.values.tolist()
        compatibleWords = self.listToWord(lsX, wordList)
        return compatibleWords

    def attemptToSolve(self): # returns number of attempts or -1 if
        global csvWordList
        wordList = csvWordList

        for i in range(0,6):
            indexLs = [1,2,3,4,5]
            badIndex = []
            goodIndex = []
            rightIndex = []
            misIndex = []
            goodW = []
            badW = []
            attemptWord = wordList[0]
            expResult = wordle.checker(attemptWord, correctWord)

            print("Attempt Word:", attemptWord)

            badIndex = [m.start() for m in re.finditer('`', expResult)]
            misIndex = [m.start() for m in re.finditer('"', expResult)]
            goodIndex = self.diff(indexLs, badIndex)
            rightIndex = self.diff(goodIndex, misIndex)

            if(len(rightIndex) == 5):
                print(attemptWord)
                print("Word Guessed Successfully")
                return(i)
            else:
                badW = self.getCharList(badIndex, attemptWord)
                goodW = self.getCharList(goodIndex, attemptWord)

                wordList = TipsHX.filter(goodW, badW)

                #this portion filters the list of words based on the characters which are at right positions
                if(len(rightIndex)>0):
                    rightW = self.getCharList(rightIndex, attemptWord)
                    wordList = self.filterCorrectCharWords(wordList, rightIndex, rightW)
        #end for
        print("Unable to guess the word in 6 tries")

