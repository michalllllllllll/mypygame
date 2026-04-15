from OOP.Product import Product

productList = []
with open("data.txt", "r") as file:
    for line in file:
        item = line.strip().split()
        productList.append(Product(item[0], item[1], True if item[2]=="True" else False, float(item[3])))

print("Printing all the data from the file which was stored in a list")
for x in productList:
    print(x)