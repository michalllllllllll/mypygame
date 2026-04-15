'''
In this module we will learn about lists in python
a list is a collection which is ordered and 
changeable. in python lists are written with square
brackets []
Arrays on the other hand are usually fixed in 
size and can have only one data
Lists allow to duplicate members
nums = [1, 2, 3, 4, 5]
names = list() #creates an empty list
to add elements to a list we use append() method
names.append("Alice")
names.append("Bob")

grade = [] 

To access elements in a list we use indexing
e.g. To access the third third element in nums
nums [2] #returns 3

To find out the length of a lit we use len()
function len(nums) returns 5
therefore the maximum index in a list is len(list) - 1

'''
# nums = []
# print(len(nums))
# nums.append(1)
# nums.append("2")
# nums.append(2,3)
# print(len(nums))
# print(nums)
'''
names = []
name = input("Enter your name: ")
while name != "-1":
    names.append(name)
    name = input("Enter your name: ")
print(names)
'''
#ex2 ask user to input numbers
#with sentinel "end":
#output the sum of all the numbers and avarage 
#value.
'''
nums = []
num = int(input("enter a number: "))
while num != "end":
    nums.append(num)
    num = input("enter a number: ")

x = len(nums)
sum = 0
while sum >= 0:
    sum == sum + ((nums)[0])
    ((nums)[0]) == ((nums)[0]) + 1
print("sum of the given numbers is", sum)
'''
'''
#ex3: ask user to input a number and output if it exist in the following
#list. nums = [4, 1, 0, 3, 2, -5, 11, 90, 3, 21]
nums = [4, 1, 0, 3, 2, -5, 11, 90, 3, 21]
num = int(input("Enter a number to search: "))
index = 0
isFound = False
while index < len(nums):
    if num == nums[index]:
        print("found value at index", index)
        isFound = True
        break
    index += 1
if not isFound: # or u can type  if isFound == False:
    print("Not found in the given array")
'''
#above algorithm will output all instances of num
# #ex4: find a user input value in a given arrayand output
# how many instances of the given values are in the array
nums = [0, -1, -4, 2, -1, 0, 4, 2, -2, 1, 2, 4, 2, 2, 6, 7, 2]
num = int(input("enter a number: "))
index = 0
isFound = False
m = 0
while index < len(nums):
    if num == nums[index]:
        print(num, "located at", index)
        m +=1
    index += 1
print("number was found",m, "times")