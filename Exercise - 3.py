#Exercise 3
#Take any list myList and write a program that prints out all the elements of the list which are less than 10.

#Extras1: Instead of printing the elements one by one, make a new list that has all the elements
#less than 10 from this list in it and print out this new list.
#
#Extras2: Ask the user a number and return a list that contains only elements from
#the origional list that are smaller than that given number.

myList = [1,2,5,7,9,23,26,35]
for i in myList:
    if int(i) < 10:
        print(i)
        
#Extras1:
newList = [i for i in myList if int(i)<10]
print(newList)

def findlessnumber(array, number) :
    for i in array:
        if int(i) < number:
            print(i)
            
num = int(input('Type one number to compare to the list'))
findlessnumber(myList,num)
