    #Exercise 9
#generate a random number between 1 and 9(both inclusive). 
#Ask the user to guess the number then tell them wheather they guessed too low, too high or exactly right

#Extras1: - Keep the game going till the user types 'exit'
#keep track of how many guesses the user has taken and when the game ends, print this out.


#Generate the random number:
import numpy as np
rNumber = np.random.randint(1,9)
count = 0

while(True):
    #Asking the user to guess the number
    guessnumber = input('Please type your guess number or exit to stop the game:')
    
    #Verifying if the user wants to stop
    if guessnumber == 'exit':
        break
    #Validating the user guess
    elif rNumber == int(guessnumber):
        count += 1
        print('Congratulations !! You have typed {} and the random number is {}'.format(guessnumber,rNumber))
        break
    elif int(guessnumber) > rNumber:
        count += 1
        print('Error ! you guessed number {} is greater than the random number{}'.format(guessnumber, rNumber))
    else:
        count += 1
        print('Error ! you guessed number {} is less than the random number{}'.format(guessnumber, rNumber))

#Verifying how many guesses the user has taken
print('You have types {} guesses'.format(guessnumber))
print('The random number was {}'.format(rNumber))
    
        