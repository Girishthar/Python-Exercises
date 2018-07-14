#Exercise 5
#Take lists say for example below lists: -
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12]
#And write a program that returns a list that contains only the elements that are 
#common to both the lists(Without dups). Make sure that program works on different sizes of lists.

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#Create  new array to pupulae the common values between two lists
commonList=[]


for i in a:
    if b.count(i) and commonList.count(i) == 0:
        commonList.append(i)
        
print('The common elements between two lists are:',commonList)