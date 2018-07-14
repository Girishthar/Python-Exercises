#Exercise 14: -
#Write a function that takes a list as input and returns a new list which are unique(No Duplicates)



def uniqueList(array):
    unique = set()
    for i in array:
        unique.add(i)
    return unique

#create lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13]

newList = uniqueList(a)
print('New list without duplicated elements ',newList)

newList = uniqueList(b)
print('New list without duplicated elements ',newList)

#Set function() : It returns an empty set(To initiliaze the array variable)
#variable.add(): - This function is used to add the elements in an empty set UNIQUE.