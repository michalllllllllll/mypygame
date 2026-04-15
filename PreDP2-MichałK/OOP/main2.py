from OOP.astro import SolarSystem, Planet

#the below constructor works even if we only pass one value
solarsyslist = []
with open("SolarSystem.txt", "r") as file:
    file.readline()
    # readData = file.readline().strip().split()
    for line in file:
        data = line.readline().strip().split(",")
        solarsyslist.append(SolarSystem(data[0],data[1],data[2],data[3]))


# planetList = []
# planetList.append(Planet(readData[3].strip()))
# AlphaC = SolarSystem(readData[0], readData[1], readData[2], readData[3])
