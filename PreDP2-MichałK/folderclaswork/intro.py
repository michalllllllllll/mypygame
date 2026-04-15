#this is how one creates a single line comment
# bobas

'''
multiple comments are creting using quote (',")
bobas
'''

# How do we create variables in Python
'''
example num = 10 
A variable to which we assign value must always be to the left.
In the flowcharts we use <- this arrow as assignment operator.
In python it is replaced by = sign
Rules of creating a variable:
1. it must start with an alphabet or _
2. Numbers can be used in the variable name but not at the start e.g.
num1 : valid variable name
2num : not okay
3. NO special characters are allowes in a variable except _
e.g digit sum : invalid variable name
digit_sum : valid variable names

Connections/Suggested rules:
1. The variables name must be meaningful
e.g. studentname, is18, 
2. Use camel case in case of longer variable names
e.g. studentClass, studentGrade
3. Keep variable names short
e.g. #boolyblud
'''

'''
# output in Python
# Use "" for texts to be displayed 
# and use variable names without quote to display their value
num = 10
print("This is how you output in Pyhton", num)

# input in Python.()
num = input() #this is how you accept a user input in python
num = int(input()) #this is how you accept a user input as a number
print(num)
# input in Python.()
num = input("Enter name: ") #this is how you accept a user input in python
num = int(input("Enter number: ")) #this is how you accept a user input as a number
print(num)
'''

'''
The input function always takes input as string (str)5
"4", 4
'''
# #condition in python:
# #example. check if a given number is even or odd
# num = int(input("Enter number: "))
# if num % 2 == 0: # use == for comparison and = for assignment
#     print(num, "is even")
# else:
#     print(num, "is odd")

# # ex2 check if a given number is positive, negative or zero
# num = int(input("Enter number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("negative")
# else:
#     print("Zero")

# #example 3 generate multiplication table of a number up to 10
# num = int(input("Enter a number: "))
# count = 1
# while count <= 10:
#     print(num,"x", count, "=", num * count)
#     count = count + 1

#example 4: output sum of digits of numbers
# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     sum = sum + n%10
#     n = n // 10
# print ("sum of digits", sum)

    
#ex5: output reverse of a number

# num = int(input("enter a number: "))
# x = 0
# while num > 0:
#     x = num % 10
#     print(x)
#     x = 0
#     num = num//10

#arrays - are list which has only one type
#and data