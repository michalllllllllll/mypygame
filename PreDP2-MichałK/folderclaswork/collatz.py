'''
Collatz conjecture

if n is even then n <- n/2
else n <- 3n + 1
repeat until n become 1.
output number o steps
'''

n=int(input("Input a number: "))
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
        count = count + 1
    else:
        n = 3 * n + 1
        count = count + 1
print(count) 