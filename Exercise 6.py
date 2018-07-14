#Exercise 6
#Ask the user for a string and check whether its a palindrome or not.
#(Pallindrom string is a one which is symmetrical eg 16561)

string = input('Please type a string:')
string[::-1]

if string ==string[::-1]:
    print('The string {} is a palindrome'.format(string))
else:
    print('The string {} is not a palindrome'.format(string))