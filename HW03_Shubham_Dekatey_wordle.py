import HW03_Shubham_Dekatey_ui as ui

# correctWord = ""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def checker(word_inp, correctWord):
    #global correctWord

    # Save a temporary copy to ensure no manipulation to actual data
    tempWord = correctWord
    resultString = ""

    print("Processing word: ", word_inp)
    for index in range(0, len(word_inp)):
        if(correctWord[index] == word_inp[index]):
            tempWord = tempWord.replace(word_inp[index], "", 1)
            resultString += " "
        elif (tempWord.find(word_inp[index]) > -1):
            tempWord = tempWord.replace(word_inp[index], "", 1)
            resultString += '"'
        else:
            resultString += "`"
    print(word_inp)
    print(resultString)

def init():
    #global correctWord
    correctWord = ui.initWordle()
    correctWord = correctWord.upper()
    print("Correct: " + correctWord)
    # loop for 6 unique input of strings
    attempts = []
    for i in range(1, 7):
        inWord = ui.acceptInput(i, correctWord, attempts)
        #attempts.append(inWord)
        checker(inWord, correctWord)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()

#   The UI file imports Dictionary file
#   The dictionary file has only 1 function to filter and return a random 5 letter word
#   Also, we can use the commented lines to get any random word from the list and the entire code would still work
#   The wordle file imports UI
#   First we establish a new random word, which is the question
#   Then a loop is run 6 times for 6 attempts of user input
#   This is done by calling acceptInput function from UI file
#   After accepting the input similar validation is performed from last submission
#   a valid input is then sent to the checker function in Wordle file
#   Checking is similar to last submission
#   with the changes introduced in last lecture (blank - correct; ["] - incorrect position, and [`] - incorrect letter)
#
#   Following is a sample output
#
# Correct: ANGER
# Attempt:  1
# Enter your value (Only first 5 characters will be considered): angel
# Your word: angel
# Enter [y/n]: y
# Processing word:  ANGEL
# ANGEL
#     `
# Attempt:  2
# Enter your value (Only first 5 characters will be considered): ajorb
# Your word: ajorb
# Enter [y/n]: y
# Processing word:  AJORB
# AJORB
#  ``"`
# Attempt:  3
# Enter your value (Only first 5 characters will be considered): angel
# Your word: angel
# Enter [y/n]: y
# Similar attempt exists.
# Attempts:  ['angel', 'ajorb']
# Re-enter the word
# Enter your value (Only first 5 characters will be considered): mango
# Your word: mango
# Enter [y/n]: y
# Processing word:  MANGO
# MANGO
# `"""`
# Attempt:  4
# Enter your value (Only first 5 characters will be considered): paris
# Your word: paris
# Enter [y/n]: y
# Processing word:  PARIS
# PARIS
# `""``
# Attempt:  5
# Enter your value (Only first 5 characters will be considered): anisl
# Your word: anisl
# Enter [y/n]: y
# Processing word:  ANISL
# ANISL
#   ```
# Attempt:  6
# Enter your value (Only first 5 characters will be considered): yorke
# Your word: yorke
# Enter [y/n]: y
# Processing word:  YORKE
# YORKE
# ``"`"