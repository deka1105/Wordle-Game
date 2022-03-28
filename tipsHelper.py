from glob import glob
from unittest import result
from HW03_Shubham_Dekatey_ui import UiX as ui
from HW03_Shubham_Dekatey_wordle import WordleX as wordle
from HW03_Shubham_Dekatey_dictionary import DictionaryX as dictionary
import pandas as pd

class TipsHX:
    csvWordList = []
    # goodWords = []
    # badWords = []
    result = []
    def __init__(self):
        #read csv
        global csvWordList
        try:
            data = pd.read_csv("wordRank.csv")
            csvWordList = data['word'].tolist()
        except:
            print("wordRank.csv File Reading error")
    
    def filter(goodW, badW):
        global csvWordList, result
        
        # if both the lists are empty, return top 50 from WordRank.csv

        if((goodW == None) & (badW == None)):
            print(csvWordList[:50])
        
        # if only good words are given, return the first 50 words containing elements from good words 

        elif((goodW != None) & (badW == None)):
            for x in csvWordList:
                if(len(result) < 50):
                    flag = 0
                    for y in goodW:
                        if(x.find(y)!= -1):
                            flag = flag + 1
                    if(flag == len(goodW)):
                        result.append(x)
                else:
                    return result
        
        # if only bad words are given, return the first 50 words not containing elements from bad words 

        elif((goodW == None) & (badW != None)):
            for x in csvWordList:
                if(len(result) < 50):
                    flag = 0
                    for y in badW:
                        if(x.find(y)== -1):
                            flag = flag + 1
                    if(flag == len(badW)):
                        result.append(x)
                else:
                    return result
        
        # return the first 50 words containing elements from good words which do not contain any bad words

        else:
            for x in csvWordList:
                if(len(result) < 50):
                    flagG = 0
                    flagB = 0
                    for y in goodW:
                        if(x.find(y)!= -1):
                            flagG = flagG + 1
                    for y in badW:
                        if(x.find(y)== -1):
                            flagB = flagB + 1
                    if((flagG == len(goodW)) & (flagB == len(badW))):
                        result.append(x)
