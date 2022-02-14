def getWordfromFile():
    import random
    my_word = ""
    # my_word = random.choice(open('words.txt').read().split()).strip()
    # print(my_word)
    # return(my_word)
    allWordList = open('words.txt').read().split()
    lenWordList = []
    for i in allWordList:
        if len(i) == 5:
            lenWordList.append(i)
    my_word = random.choice(lenWordList)
    return my_word