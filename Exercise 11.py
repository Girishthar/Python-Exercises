#Exercise 11
# Ask the user for a number and check whether its a prime or not.

#Creating a function if the number is a prime or not

def findprime(num):
    divisors = [x for x in range(1, num+1)
                if num % x == 0]
    if len(divisors) > 2:
        print('This number {} is not a prime number'.format(num))
    else:
        print('This number {} is a prime number'.format(num))

#Asking for a number
prime = int(input('Type a number to know whether its a prime or not:'))

#Call function
findprime(prime)