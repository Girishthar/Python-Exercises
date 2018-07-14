#Exercise 8
#Make a two player Rock paper scissors game.
#Rules

#Rock beats Scissors
#Scissorts beats Paper
#paper beats Rock

stop = False
while(not stop):
    
    #Asking answer to the player 1
    answerP1 = input('Player 1: Please type your choice: Rock, Paper or Scissors:')
    
    #Asking answer to the player 2
    answerP2 = input('Player 1: Please type your choice: Rock, Paper or Scissors:')
    
    #Comparing the responses according to the Rock-Paper-Scissors game rule
    if answerP1 == answerP2:
        print('Draw Game')
    elif answerP1 == 'Rock' and answerP2 == 'paper':
        print('Player 2 Wins')
    elif answerP1 == 'Rock' and answerP2 == 'Scissors':
        print('Player 1 wins')
    elif answerP1 == 'Paper' and answerP2 == 'Rock':
        print('PLAYER 1 WINS')
    elif answerP1 == 'Paper' and answerP2 == 'Scissors':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Scissors' and answerP2 == 'Rock':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Scissors' and answerP2 == 'Paper':
        print('PLAYER 1 WINS')
    else:
        print('Wrong answer, please type Rock, Paper or Scissors in your next attempt!')
        
    #asking to the user if he wants to start a new game or cancel
    answer = input('Do you want to start a new game? (Yes or No)')
    
    #asking to the user if he wants to start a new game or cancel
    if answer == 'Yes':
        print('New game will start')
    elif answer == 'No':
        stop = True
        print('GAME OVER')
    else:
        print('Wrong answer, please type Yes or No in your next attempt!')
    
    
