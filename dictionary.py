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
    sWord = difflib.get_close_matches(word,data)[0] # Geting similiar word
    answer = None
    errorMSG = "Not able to find the word or similar one. Please, check it."

    # Checking wether the word exist.
    if word in data:
        # Case it exists, returning the definition.
        return data[word]
    
    # Checking wether there are any similar word
    elif len(sWord) > 0:
        # Confirming the word
        while answer != 'y' and answer != 'n':
            answer = input("Did you mean %s instead? please, type Y or N: " % sWord)
            answer = str(answer.lower())
        
        if answer == 'y':
            return data[sWord]
        else:
            return errorMSG

    # Case it does not, returning the error message.
    else:
        return errorMSG
    
### Starting the program ###
# Asking input word from user
word = input("Please, inform the word: ")

# Output the results #
print(locate(word))
