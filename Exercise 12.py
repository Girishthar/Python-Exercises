#Exercise 12
#Write a program that takes list of numbers and makes a new list of
#only the first and last elements. For practice use the functions.

def findFirstLast(anylist):
    temp = []
    temp.append(anylist[0])
    temp.append(anylist[-1])
    return temp

a = [5,10,15,20]

print('A new llist with first and last element is {}'.format(findFirstLast(a)))