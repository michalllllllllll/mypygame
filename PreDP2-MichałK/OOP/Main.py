from OOP.Intro2OOP import Student
from OOP.Product import Product

# Maks = Student("Maks", 13, "9A")
# print(Maks.age)

# Pankaj = Student("Pankaj", 100, "None")
# print(str(Pankaj))
# print(str(Maks))
# print(Student.studentsNum)
# Merry = Student("Merry", 20, "12B")
# print(Student.studentsNum)
# print(Student.studentNum())

# str(Student)
# milk = Product("Milk", "Food", True, 4.99)
# milk.cost(10)
# # print(milk)
# listProducts = []#this will contain objects of Product
# listProducts.append(milk)
# listProducts.append(Product("Bread","Food", True, 0.7 ))
# listProducts.append(Product("Apple", "Food", True, 1.23))

# data.txt/data.csv
# #we need to ask user to input values for a given product
# run = True #this will determine how long should we keep accepting user input
# while run:
#     name = input("Enter product name: ")
#     cat = input("Enter category- food, clothing, cosmetics: ")
#     e = input("Is it essential: 1 else 0: ")
#     isE = True if e == "1" else False
#     while True:
#         try:
#             p = float(input("Enter cost for the product: "))
#             break
#         except:
#             print("Something went wrong")
#     #writing to a file in Python
#     item = Product(name, cat, isE, p)
#     with open("data.txt", "a") as file:
#     #.csv file fromat refers to comma seperated value
#     #w: write - anytime we open the file to write it it will erase the old data and only keep the new data
#     #a: append - this will append to the file
#         file.write(str(item)+"\n")
#     r = input("Enter 1 if you wish to continue adding more products: ")
#     run = False if r != "1" else True

#     #input 5 objects into the persistent storage (file)


