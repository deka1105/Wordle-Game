import re
word = "SONAR"
attempts = []
# loop for 6 unique input of strings
for i in range (1, 7):
    valid_inp = 0
    print("Attempt: ", i)

    #Loop till a valid attempt is made
    while(valid_inp == 0):
        word_inp = input("Enter your value (Only first 5 characters will be considered): ")
        word_inp = word_inp[:5]

        #Check input length, should be greater than length of word
        if(len(word_inp) >= len(word)):
            # Check if the first 5 characters are only alphabets
            if re.match("^[a-z, A-Z]*$", word_inp):
                print("Your word:", word_inp)

                #Seek confirmation to proceed
                confirmation = input("Enter [y/n]: ")
                if((confirmation == 'y') or (confirmation == 'Y')):
                    #check for existing attempts
                    if(i > 0):
                        if word_inp in attempts:
                            print("Similar attempt exists.")
                            print("Attempts: ", attempts)
                            print("Re-enter the word")
                        else:
                            attempts.append(word_inp)
                            valid_inp = 1
                else:
                    print("Re-enter the word")
            else:
                print("Word can contain only Alphabetic values [A-Z] or [a-z]")
        else:
            print("Re-enter a word with atleast 5 alphabetic characters")
    # Convert input string to upper case for better comparison
    word_inp = word_inp.upper()

    # Save a temporary copy to ensure no manipulation to actual data
    tempWord = word
    print("Processing word: ", word_inp)
    for index in range(0, len(word_inp)):
        if(word[index] == word_inp[index]):
            #remove 1 instance of character from temoporary copy
            tempWord = tempWord.replace(word_inp[index], "", 1)
            print(word_inp[index], "Green")
        elif (tempWord.find(word_inp[index]) > -1):
            tempWord = tempWord.replace(word_inp[index], "", 1)
            #print(word)
            print(word_inp[index], "Yellow")
        else:
            print(word_inp[index], "Red")


##
#PSEUDO CODE
# Store the values of Word to be found (in this case SONAR)
# Initialize attempt list
# Loop a counter for the number of attempts (in this case 5)
#     Accept input from the user
#     length of input should be more than 5, else re-enter
#     strip the input to the first 5 characters
#     check for only alphabetic data, else re-enter
#     ask for user confirmation, else re-enter
#     check previous attempts, if present allow retry
#     Update the attempt counter and add to attempt list
#
#     Convert the input to upper case
#     Make a temporary copy of the word
#     Loop index counter till the length of word (len(SONAR) = 5)
#         if the same characters are at the index counter, print Green and remove 1 occurrence of the variable from the word
#         else if the character is present in the word, print yellow & remove 1 occurrence of the variable from the word
#         else print red
