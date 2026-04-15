class Student:
    '''This class defines Student attributes'''
    studentsNum = 0#this is static variable which means it's common for the entire class
    #constructor : is a special function which is used to instantiate an object of the class
    def __init__(self, name:str, age:int, grade:str):
        self.name = name
        self.age = age
        self.grade = grade
        self.School = "2SLO Jasienicy"
        Student.studentsNum += 1

    def __str__(self):
        return f"""
Student Name   = {self.name}
Student Age    = {self.age}
Student Class  = {self.grade}
Student School = {self.School}
"""
    #This is a static function that means it is common for the entire class
    def studentNum():
        return Student.studentsNum

    