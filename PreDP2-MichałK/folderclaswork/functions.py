'''
What are functions:
Functions are reusable blocks of code that perform a specific task. 
They help to organize code, make it more readable, and allow for code reuse.
Functions can take inputs (parameters), process them, and return outputs (results). 
They are defined using the 'def' keyword in Python, 
followed by the function name and parentheses containing any parameters. 
Functions can be called multiple times throughout a program, making it 
easier to manage complex code.
'''
def test(a, b):
    #here a and b are parameter
    # test is the name of the function
    #def is a keyword that informs Python that we are defining a function
    print("This is a test function with 2 parameters.")
    print("The value of these parameters are ", a, b)

#how do we use the above defined function - this is known as "calling" a function
# test(5, True) # a function must be called to execute the code in it otherwise it never executes by itself
#the value of 5 is assigned to the paramter a
#while the value of True is assigned to teh parameter b
#5 & True are called arguments which we pass to parameters with which the function was defined
# test(1, 2)

#we want to create functions that will convert from Denary to other systems
def toBinary(num):#the binary value will be stored as a string
    bNum = ""
    while num>0:
        s = num % 2
        num = num // 2
        bNum = str(s) + bNum
    print(bNum)
    return bNum

def toOctal(num):
    oNum = ""
    while num>0:
        s = num % 8
        num = num // 8
        oNum = str(s) + oNum
    print(oNum)
    return oNum

def toHexa(num):
    hNum = ""
    while num>0:
        s = num % 16
        num = num // 16
        hNum = checkAlpha(s) + hNum
    print(hNum)
    return hNum

def checkAlpha(n):
    match n:
        case 10:
            return 'A'
        case 11:
            return 'B'
        case 12:
            return 'C'
        case 13:
            return 'D'
        case 14:
            return 'E'
        case 15:
            return 'F'
        case _:
            return str(n)

def toBase(num: int, base: int):
    #this can convert any denary to any base upto 16
    hNum = ""
    while num>0:
        s = num % base
        num = num // base
        hNum = checkAlpha(s) + hNum
    print(hNum)
    return hNum

def bi2base(bNum: str, base: int):
    #first we conver binary to denary
    l = len(bNum)-1
    i = 0
    dNum = 0
    while i<=l:
        dNum += int(bNum[i])*2**(l-i)
        i+=1
    dNum = toBase(dNum, base)
    # print(dNum)
    return dNum

def oct2base(onum:str, base: int):
    l = len(oNum)-1
    i = 0
    dNum = 0
    while i<=l:
        dNum += int(oNum[i])*8**(l-i)
        i+=1
    dNum = toBase(dNum, base)
    # print(dNum)
    return dNum

def checkNum(k):#k is an alphabet which we need to convert to base 10
    match k.upper(): #by converting it to upper case we make it case insensitive
        case 'A':
            return 10
        case 'B':
            return 11
        case 'C':
            return 12
        case 'D':
            return 13
        case "E":
            return 14
        case 'F':
            return 15
        case _:
            return int(k)

def hex2base(hnum:str, base: int):
    l = len(hnum)-1
    i = 0
    dNum = 0
    while i<=l:
        dNum += checkNum(hnum[i])*16**(l-i)
        i+=1
    dNum = toBase(dNum, base)
    # print(dNum)
    return dNum

def toanyBase(num: str, base:int, tobase: int):
    if base == 10:
        return toBase(int(num), tobase)
    else:
        #convert num from base to denary
        l = len(num)-1
        i = 0
        dNum = 0
        while i<=l:
            dNum += checkNum(num[i])*base**(l-i)
            i+=1
        return toBase(dNum, tobase)


toanyBase("123", 4, 10)


# toBinary(8)
# toHexa(255)
# toBase(123, 11)
# bi2base("11111111", 8)
hex2base("a10", 4)

# test(toBinary(16), toOctal(16))

