from HW03_Shubham_Dekatey_dictionary import DictionaryX as di
from logger import LogX as log
import re
# word = ""
# wordLength = 0
# attempts = []

class UiX:


    globalAttempts = []

    def initWordle():
        try:
            global word, wordLength
            di.filterletterWord(5)
            word = di.getWordfromFile()
            wordLength = len(word)
            return word
        except:
            return("_")
            print("Game ui.initWordle Error")


    def __init__():
        try:
            global word, wordLength
            di.filterletterWord(5)
            word = di.getWordfromFile()
            wordLength = len(word)
            return word
        except:
            print("Game ui.initWordle Error")

    def __str__(self):
        return f"Ui(userInputList:{str(self.globalAttempts)})"

    def initWordle():
        try:
            global word, wordLength
            di.filterletterWord(5)
            word = di.getWordfromFile()
            wordLength = len(word)
            return word
        except:
            print("Game ui.initWordle Error")

    def acceptInput(i, word, attempts):
        globalAttempts = attempts
        try:
            valid_inp = 0
            wordLength = len(word)
            print("Attempt: ", i)
            log.writeLog("Attempt: " + str(i))
            # global attempts
            # Loop till a valid attempt is made
            while valid_inp == 0:
                word_inp = input("Enter your value (Only first " + str(wordLength) + " characters will be considered): ")
                word_inp = word_inp[:wordLength]

                # Check input length, should be greater than length of word
                if len(word_inp) >= len(word):
                    # Check if the first wordLength characters are only alphabets
                    if re.match("^[a-z A-Z]*$", word_inp):
                        print("Your word:", word_inp)
                        log.writeLog("Your word:"+ word_inp)
                        word_inp = word_inp.upper()
                        # Seek confirmation to proceed
                        confirmation = input("Enter [y/n]: ")
                        if (confirmation == 'y') or (confirmation == 'Y'):
                            # check for existing attempts
                            if i > 0:
                                if word_inp in attempts:
                                    print("Similar attempt exists.")
                                    log.writeLog("Similar attempt exists.")
                                    print("Attempts: ", attempts)
                                    log.writeLog("Attempts: ", str(attempts))
                                    print("Re-enter the word")
                                    log.writeLog("Re-enter the word")
                                else:
                                    if(di.checkWordExists(word_inp)):
                                        attempts.append(word_inp)
                                        valid_inp = 1
                                    else:
                                        print("Not a Dictionary word. Try Again")
                                        log.writeLog("Not a Dictionary word. Try Again")
                        else:
                            print("Re-enter the word")
                            log.writeLog("Re-enter the word")
                    else:
                        print("Word can contain only Alphabetic values [A-Z] or [a-z]")
                        log.writeLog("Word can contain only Alphabetic values [A-Z] or [a-z]")
                else:
                    print("Re-enter a word with atleast" + wordLength + "alphabetic characters")
                    log.writeLog("Re-enter a word with atleast" + str(wordLength) + "alphabetic characters")
            # Convert input string to upper case for better comparison
            word_inp = word_inp.upper()
            #attempts.append(word_inp)
            return word_inp
        except:
            print("Game ui.acceptInput Error")
            


