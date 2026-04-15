# '''
# This file contains programs which shows how to work with String data type.
# A string data type basically means that the values stored are charaters.
# Even if they are numbers but stored as string type then they cannot be utilised 
# for math operations unless they are converted to integer type or float type.
# Several data types:
# 1. numeric :
#     a. integer - stores whole numbers
#     b. float - stores decimal place values 
# 2.characters
#     a. - string - stores any printable characters. Many char characters put together
#     b. char - this refers to a single character
#     e.g. = "Python" - this is a string type
#     and every character in the above string in a char type 
#     "p" "y" "t" "h" "o" "n"  - these are char types
# 3.boolean - stores True or False value
# '''
# '''
# s1 = "Python"
# w = "Welcome"
# ver = "3"
# ver_1 = 3
# msg = w + " to " + s1+ver
# print(w, "to", s1)
# print(msg)
# print("Length of the variable msg =", len(msg))
# tentimes = s1 * 10
# print(tentimes)
 
# #we want to extract substrings from a given string
# #from variable s1 - we only want to extract "Py"
# subS1 = s1[0:2]
# print(subS1)
# #now only extract th from s1
# subS1_2 = s1[2:4]
# print(subS1_2)
# '''
# '''
# *
# **
# ***
# ****
# *****
# '''
# '''
# n = int(input("enter a number of rows: "))
# est = "*"
# row = 1
# while row <= n:
#     print(est*row)
#     row += 1
# '''
# '''
# ex2. generate the following pattern
# for n = 5
#     *
#    ***
#   *****
#  *******
# *********
# '''

# '''
# n = int(input("enter a number of rows: "))
# est = "*"
# row = 1
# col = " "
# t = 1
# while row <= n:
#     col *= (t-row)
#     row *= (2*row - 1)
#     print (col, est)
#     row += 1

# print()
# '''

# #ex3: for n= 5
# '''
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# '''

# # n = int(input("enter a number of stars that you want to achieve: "))
# # row = 1
# # col = "*"
# # while row <= n:
# #     col = 1
# #     while col <= row:
# #         print ("*", end="")
# #         col = col + 1
# #     print()
# #     row = row + 1
# # row = 1
# # while row <= n-1:
# #     col = 1
# #     while col <= n - row:
# #         print("*", end="")
# #         col += 1
# #     row += 1
# #     print()

# # n = int(input("enter a number of stars that you want to achieve: "))
# # b = n
# # est = "*"
# # row = " "
# # while n>0:
# #     print(row, est)
# #     while n>= 0:
# #         row += 1
# #     print()

# '''
# n = int(input("enter a number of rows: "))
# est = "*"
# row = 1
# col = " "
# t = 1
# m = n - 1
# while row <= 2*n:
#     print (col*m, est*row)
#     t -= 1
#     row += 2
#     m = m -1

# '''
# '''
# #ex 3
# n = int(input("enter a number of rows: "))
# est = "*"
# row = 1
# t = 1
# m = n - 1
# while n >= t:
#     print (est*t)
#     row += 1
#     t += 1


# while n >= 0:
#     print (est*t)
#     row += 1
#     t -= 1
#     n -= 1
# '''
# '''
# #ex4
# n = int(input("enter a number of rows: "))
# est = "*"
# row = 1
# col = 1
# t = 1
# p = " "
# m = n - 1
# i = 1
# while n >= m:
#     print (p*m, est*t, p*m, est*t)
#     row += 1
#     m += 1
# '''

# # ex5
# n = int(input("enter a number of rows: "))
# est = 11
# row = 1
# col = " "
# t = 1
# m = n - 1
# while row <= 2*n:
#     print (col*m, est*row)
#     t -= 1
#     row += 2
#     m = m -1
#     est  == 11^2

# print("program outputting  frequency of all vowels in a given sentence")  
# n = input("Enter a sentence: ")
# vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# for char in n:
#     if char in vowels:
#         vowels[char] += 1

# total_vowels = sum(vowels.values())

# print("Total vowel count =", total_vowels)
# for vowel in vowels:
#     print(f'"{vowel}" count = {vowels[vowel]}')