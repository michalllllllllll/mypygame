#ex 2 generate the following pattern for n = 5
'''
    *
   ***
  *****
 *******
*********
'''
'''
n = int(input("Enter a number of rows: "))
row = 1
while row <= n:
    col = 1
    #to print empty spaces
    while col <= n - row:
        print(" ", end="")
        col += 1

    #to print
    col = 1
    while col<= 2*row -1:
        print("*", end="")
        col += 1

    row += 1
    print()
'''
#ex3 for n = 5
'''
*
**
***
****
*****
****
***
**
*
'''
'''
n = int(input("enter a number of stars that you want to achieve: "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print ("*", end="")
        col = col + 1
    print()
    row = row + 1
row = 1

row = 1
while row <= n-1:
    col = 1
    #to print empty spaces
    while col <= n - row:
        print("*", end="")
        col += 1
    row += 1
    print()
'''

