# Welcome to the first python class

'''

OutLines:
Variables /Values / Operators
Operator
Arithmetic Operator
print (x + y) Addition 
print (x - y) Subtraction
print (x * y) Multiplication 
print (x / y) Divition 
Python Data Types :
     Strings 
     e.g name = 'Bolu'
         name2 = 'Parach'
         statement = ' Hello, welcome to the first python class'
         statement2 = '' He's coming to the party''
        note... (if you use single quotation inside, you will use double outside) 
     Integer: Numbers,Float,complex 
     Collection : List, Tuple, Set, Dict

Control Statemeents:
    Conditional Statement 
    Loops / Iteration

Function 
Classes
Project

'''

x = 5
y = 10
name = 'Boluwatife'
print(name[6:10])
print(name.capitalize ())
print(name.upper ())
print(name.lower ())

statement = 'Boluwatife'
# Assignment 
# write out at least 10 string method  and utilize
# COUNT =Returns the numbers of times a specilized value occurs in a string 
name = 'tolulope is a girl'
print(name.count('girl'))
# ENDS WITH = returns true if the string ends with the specified value 
print(name.endswith('e'))
#format = specified values in a string
print(name.format('name','description')) 
#ISUPPER= RETURNS TRUE IF ALL CHARACTERS IN THE STRINGS ARE UPPER CASE
print(name.isupper()) 
# swapcase = swaps cases,lower case become upper case and vice versa
print(name.swapcase())
#SPLIT = SPLITS THE STRINGS AT THE SPECIFIED SEPERATOR AND RETURNS A LIST
print(name.split(','))
#TRANSLATE = RETURNS A TRANSLATE STRING 
print(name.translate('girl'))
#TITLE = CONVERT THE FIRST CHARACTER OF EACH WORD TO UPPERCASE
print(name.title())
#EXPAND TAB
#REPLACE
           