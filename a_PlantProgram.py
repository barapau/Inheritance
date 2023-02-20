import a_PlantClass as pc

primrose = pc.Plant("Green") #instance called primrose

sunflower = pc.Flower("Yellow", 12) #instancee of my subclass

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals()) #this doesnt work because primrose
                             #is a superclass,  it does contain
                             #attributes for a subclass
