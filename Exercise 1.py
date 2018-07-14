#Exercise 1: - 
#Create a function which will take name and age as input and will calculate the year at which user will be completing the 100 years.

#import datetime function
import datetime

#Asking name
name = input('Type your name:')

#Asking age
Age = input('Type you age:')

#get the current date year
Today_year = datetime.datetime.now()

#get the difference between between age and 100 years
diff = 100 - int(Age)

#Show the year that user will turn 100 years old
print('Hi ' + name + ' you will complete 100 years in:' , (Today_year.year+diff))