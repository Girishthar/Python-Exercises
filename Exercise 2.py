#Ask the user to enter a number, depending on whether number is even or odd, respond the user
#Also If the the number is divided by 4, send a differenta message
#Ask the user for two numbers: - One is to check(Num1) and one number to divide by(Num2).
#If Num2 divides evenly into Num1, tell that to the user, if not send an appropriate message.


Num1 = int(input('Type a number to verify whether its odd or even:'))

#Verifying its odd or even: -
if Num1 / 2 == 0:
    print('The number {} is even'.format(Num1))
else:
    print('The number {} is odd'.format(Num1))
    
#If number is multiple of 4, put a different message
Num1 = int(input('Type a number to verify whether its odd or even:'))

if Num1 % 4 == 0:
    print('The number {} is even a divisible by 4'.format(Num1))
elif Num1 % 2 == 0:
    print('The number {} is even '.format(Num1))
else:
    print('The number {} is odd'.format(Num1))
    

#Exercise for divisibility test: -
Num1 = int(input('Type a number to check the divisibility'))
Num2 = int(input('Type a number to divide'))

if Num1 % Num2 == 0:
    print('The number {} divides evenly with {} and this number is even'.format(Num1,Num2))
else:
    print('The number {} does not divides evenly with {} '.format(Num1,Num2))