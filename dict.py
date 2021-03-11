#Importig libraries
import json
import difflib
from difflib import get_close_matches

#loading data
data=json.load(open("data.json"))

#Dictionary function
def translate(word):
    word=word.lower() 
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
 
 #get close matches is used to check if user mispells the word.    
 elif len(get_close_matches(word, data.keys())) >0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("Press y for yes and n for no")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide =="n":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return("wrong input")
    else:
        print("Word not found")
        
       

word=input("enter the word you want to search")
output=translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)