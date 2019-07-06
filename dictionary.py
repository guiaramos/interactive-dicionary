# DESCRIPTION #
# This interactive dictionary works by searching on JSON file.
# If the word is misspelled the program tries to find a similar word.
# Created by Guilherme Ramos.

# Libraries
import json
import difflib

### Variables ###
data = json.load(open("src/data.json", "r")) # Getting data

### Definitions ###

# Searching the word on the data basis
def locate (word):
    
    # Assigning  def variables
    word = word.lower() # Str case sensitivity = lowercase
    sWord = difflib.get_close_matches(word,data)[0] # Geting simiiar word
    answer = None
    
    #Messages
    errorMSG = "Not able to find the word or similar one. Please, check it."
    askMSG = "Did you mean %s instead? Enter Y if yes or N if no: " % (sWord)

    # Checking wether the word exist
    if word in data:
        return data[word]

    
    # Checking if the word is a city, country and so ever.
    elif word.title() in data:
        return data[word.title()]
    
    # Checking wether there are any similar word
    elif len(sWord) > 0:
        while answer != 'y' and answer != 'n':
            answer = input(askMSG)
            answer = str(answer.lower())
        
        if answer == 'y':
            return data[sWord]
        else:
            return errorMSG

    # Case it does not, returning the error message.
    else:
        return errorMSG
    
### Start of the program ###

# Asking input word from user
word = input("Please, inform the word: ")

# Assigning the search on the variable
output = locate(word)

# Output the results split by lines #
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

### End of the program ###