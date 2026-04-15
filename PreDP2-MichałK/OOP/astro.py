'''
Create a class called SolarSystem
Name
number of stars
number of planets
distance (LY)
list of planets

Create another class called Planet
attributes for this are as follows
Name
Mass
Distance from the sun/ star/ (center of mass of a star system)
num of moons

create the usual dunders in it and str
'''
class SolarSystem:
    '''This class defines solarsystem attributes'''
    
    def __init__(self, solarsystem:str, starNum:int, distance:float, list:str, planetNum: int):
        self.solarsystem = solarsystem
        self.starNum = starNum
        self.distance = distance
        self.list = list
        self.planetNum = planetNum
        starNum = 0
        planetNum = 0
        SolarSystem.starNum += 1
        SolarSystem.planetNum += 1

    def __str__(self):
        return f"""
solarsystem Name   = {self.solarsystem}
solarsystem starNum = {self.starNum}
solarsystem planetNum = {self.planetNum}
solarsystem distance    = {self.distance}
solarsystem list  = {self.list}
"""
    def solarsystemNum():
        return SolarSystem.solarsystemNum
    

class Planet:
    '''This class defines solarsystem attributes'''
    
    def __init__(self, name:str, mass:float = 0, distance:float = 0, moonNum:int = 0):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moonNum = moonNum


    def __str__(self):
        return f"""
planet Name   = {self.name}
planet mass = {self.mass}
planet distance = {self.distance}
planet moonNum  = {self.moonNum}
"""
    def planetNum():
        return Planet.planetNum
