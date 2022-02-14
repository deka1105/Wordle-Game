import HW03_Shubham_Dekatey_dictionary as di
import re

# word = ""
# wordLength = 0
# attempts = []


def initWordle():
    global word, wordLength
    word = di.getWordfromFile()
    wordLength = len(word)
    return word

def acceptInput(i, word, attempts):
    valid_inp = 0
    wordLength = len(word)
    print("Attempt: ", i)
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
                word_inp = word_inp.upper()
                # Seek confirmation to proceed
                confirmation = input("Enter [y/n]: ")
                if (confirmation == 'y') or (confirmation == 'Y'):
                    # check for existing attempts
                    if i > 0:
                        if word_inp in attempts:
                            print("Similar attempt exists.")
                            print("Attempts: ", attempts)
                            print("Re-enter the word")
                        else:
                            if(di.checkWordExists(word_inp)):
                                attempts.append(word_inp)
                                valid_inp = 1
                            else:
                                print("Not a Dictionary word. Try Again")
                else:
                    print("Re-enter the word")
            else:
                print("Word can contain only Alphabetic values [A-Z] or [a-z]")
        else:
            print("Re-enter a word with atleast" + wordLength + "alphabetic characters")
    # Convert input string to upper case for better comparison
    word_inp = word_inp.upper()
    #attempts.append(word_inp)
    return word_inp

