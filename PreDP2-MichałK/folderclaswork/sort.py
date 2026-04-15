#bubble sort
# A = [0, -4, 9, -11, 4, 6, 1, 5, 23, 6, 2, -1]
# print("before sort", A)
# n = len(A) #since we need n many times it's beteer to store it in a variable
# i = 0
# while i < n:
#     j = 0
#     while j < n-1:
#         if A[j] > A[j+1]:
#             #swap
#             t = A[j]   #t is a temporary variable 
#             A[j] = A[j+1]
#             A[j+1] = t
#         j += 1
#     i += 1
#     print("after round", i, A)
# print("after sort:", A)

#bubble sort using for loop
'''
When to use for loop instead of while loop - we use it when we exactly know
how many iterations to execute in the algorithm.
the range (a, b, c)
where a = initial value, default is 0
b = final value but excluive and you must provide the value
c= is increment or how to change the variable i. default is 1.

e.g increament value of a variable by 2
range(0, f, 2)

if the initial value is different than 0 then you must provide it
range (10, 5, -1)
'''

# A = [0, -4, 9, -11, 4, 2]
# print("before sort", A)
# n = len(A) #since we need n many times it's beteer to store it in a variable
# i = 0
# count = 0
# for i in range(n):
#     for j in range(n-1-i):
#         if A[j]>A[j+1]:
#             A[j], A[j+1], = A[j+1], A[j] #this swap works only in python
#             isSwapped = True
#         count += 1
#     print("After round", i+1, A)
#     if isSwapped == False:
#         break


# print("After sort", A)
# print( count, "rounds to complete the task")

#selection sort
'''
It works by finding the smalles/largest value
Thean place it at index 0
Then find the next smallest value ignoring index 0 and then place it at index 1
and continue until n-1 elements 
'''

#finding the smallest value in an array
A = [0, -4, 9, -11, 4, 6]
print("before sort", A)
n = len(A) #since we need n many times it's beteer to store it in a variable
i = 0
count = 0
for i in range(n-1):
    sIndex = 1
    for j in range(i+1, n):
        if A[sIndex] > A[j]:
            sIndex= j
        count += 1
    #after finding index of the smallest value - swap it with the first possible
    A[sIndex], A[i] = A[i], A[sIndex]
    print("after round", i+1, A)
print("After sort", A)
print(count)