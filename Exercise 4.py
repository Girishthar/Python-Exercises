#Exercise 4
#Create a program that takes the number from user and then prints out a list of
#all divisors of that number

#Take a number:
Number = int(input('Enter the number:'))

divisors = [i for i in range(1, Number+1) if Number % i == 0]
print('divisors:',divisors)

#Alternate: - 
#for i in range(1,Number+1):
#    if Number % i == 0:
#        print(i)