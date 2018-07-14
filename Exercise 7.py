#Exercise 7
#Alternate numbers
#Write one line of python code that takes the list and makes a new list that has only the 
#even elements of the list.

a= [1,4,9,16,25,36,49,64,81,100]

New = [x for x in a 
       if x % 2 ==0]

print('Even numbers',New)