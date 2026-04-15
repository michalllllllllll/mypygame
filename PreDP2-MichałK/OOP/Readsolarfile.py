from OOP.Product import Product

productList = []
with open("solarfile.csv", "r") as file:
    for line in file:
        item = line.strip().split()
        productList.append(Product( str(item[0]), float(item[1]), float(item[2]), float(item[3]), float(item[4]), float(item[5]), float(item[6]), float(item[7]), float(item[8])))
        print("Printing all the data from the file which was stored in a list")
for x in productList:
    print(x)