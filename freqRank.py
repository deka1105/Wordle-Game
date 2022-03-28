
from glob import glob
import logging

from logger import LogX


listWords = []
freqDict = {}
occDict = {}
allKeys = []
freqTuple = {}
freqTup = {}

def readfile():
    try:
        LogX.writeLog("Loading filterWords.txt")
        lenWordList = open('filterWords.txt').read().split()
        global listWords
        listWords = lenWordList
        return True
    except:
        print("filterWords.txt Loading error")
        LogX.writeLog("filterWords.txt Loading error")
    

    # return my_word

def freqCreator():
    # for i in range(ord('A'), ord('Z') + 1):
    #         freqDict[chr(i)] = [0,0,0,0,0]
    # for word in words:
    #         for i in range (0, len(word)):
    #             val = freqDict[word[i]]
    #         #     print(val)
    #             val[i] = val[i]+1
    #             freqDict[word[i]] = val

    # for i in range(ord('A'), ord('Z') + 1):
    #     freqDict[chr(i)] = [0,0,0,0,0]
    #     occDict[chr(i)] = 0
    #     allKeys.append(chr(i))
        
    # for word in words:
    #         for i in range (0, len(word)):
    #             val = freqDict[word[i]]
    #         #     print(val)
    #             val[i] = val[i]+1
    #             freqDict[word[i]] = val
    # #         for i in allKeys:
    # #             if word.find(i):
    # #                 occDict[i]+=1

    #         for i in allKeys:
    # #             print(i)
    #             if (str(i) in word):
    #                 occDict[str(i)]+=1
    global freqDict, occDict
    for i in range(ord('A'), ord('Z') + 1):
        freqDict[chr(i)] = [0,0,0,0,0]
        occDict[chr(i)] = 0
        allKeys.append(chr(i))
        
    for word in listWords:
            for i in range (0, len(word)):
                val = freqDict[word[i]]
                val[i] = val[i]+1
                freqDict[word[i]] = val

            for i in allKeys:
                if (str(i) in word):
                    occDict[str(i)]+=1
                
    for i in allKeys:
        #if(occDict[str(i)] != 0):
            myList = freqDict[str(i)]
            # myList[:] = [x / occDict[str(i)] for x in myList]
            myList[:] = [x / len(listWords) for x in myList]
            round_to = [round(num, 4) for num in myList]
            freqDict[str(i)] = round_to

def writeDict():
    import string
    f = open("letterFrequency.csv", 'w')
    for key in string.ascii_uppercase:
        f.write(f"{key}, {freqDict[key][0]}, {freqDict[key][1]}, {freqDict[key][2]}, {freqDict[key][3]}, {freqDict[key][4]}\n")


def tupleFromFile():
    import csv
    d = {}
    f = {}
    allKeys = []
    try:
        with open('letterFrequency.csv') as f:
            for key, *values in csv.reader(f):
                d[key] = tuple(map(str, values))
    except:
        print("CSV Reading error")

def ranks():
    freqCreator()
    word_dictionary = {}
    sorted_list = []
    for word in listWords:
        val = 1
        for i in range (0, len(word)):
            temp = list(freqDict[word[i]])[i]
            val *= temp
        word_dictionary[word] = val
    sorted_list = sorted(word_dictionary.items(), key=lambda x:x[1])
    sorted_list.reverse()
    flag = 1
    for i in range (0, len(sorted_list)):
        sorted_list[i] = sorted_list[i] + tuple(str(flag))
        flag += 1
    import csv
    with open('wordRank.csv','w') as out:
        csv_out=csv.writer(out)
        for row in sorted_list:
            csv_out.writerow(row)
    #reverse
    #stor csv
