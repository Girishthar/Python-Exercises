#Write a function that asks the user a string and reverse the order of a string(not the words)
#Example: - If a user type "My NAME IS GIRISH", our output should be "GIRISH IS NAME MY"

def backwardstring(string):
    #Spliting the sentence into words
    words = string.split(' ')
    
    #Reversing the words sequence
    for i in words:
        newwords = words[::-1]
        
    #Joining the words in sentences
    newSentence = ' '.join(newwords)
    return newSentence

string = 'Girish is mainframe developer'
backwardstring(string)
print(backwardstring(string))
    
    
    