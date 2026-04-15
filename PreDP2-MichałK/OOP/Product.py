class Product:
    '''This class describes a product which has 
    the following attributes.
    pName = Product Name
    cName = Product category name [Food, Cosmetics, Electronics]
    isEssential = boolean variable which indicates whether the product is essential or not
    price = floating point value

    '''
    #create constructor with the above attrributes defined
    #create a static variable to count number of products
    #create str method to display all the properties
    #create a method called cost(numOfItems)-> return price * numOfItems
    #In the main.py create 2 objects of this class and use the methods
    #to demonstrate if your code works

    productNum = 0

    def __init__(self, pName:str, cName:str, isEssential:bool, price:float):
        self.pName = pName
        self.cName = cName
        self.isEssential = isEssential
        self.price = price

    def __str__(self):
        return f"""{self.pName}, {self.cName}, {self.isEssential}, {self.price}"""
    
    def cost(self, numOfItems:int):
        return self.price*numOfItems