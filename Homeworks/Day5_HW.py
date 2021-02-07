class Animal(): #parent
    counter = 0
    def __init__(self,name, color, age, numberofLegs = 4):

        print("Animal is called.")
        self.name = name
        self.color = color
        self.age = age
        self.numberofLegs = numberofLegs
        Animal.counter += 1

    def walk(self):
        print("Animals can walk.")

#inherited from Animal class
class Dogs(Animal): #child1

    def __init__(self,name, color, age,  food, numberofLegs = 4):
        super().__init__(name, color, age, numberofLegs)
        print("Dog class is called")
        self.food = food

    def bark(self):
        print("Dogs bark")

    def propertiesDog(self):
        print("This dog's name is {}, and its age is {}.".format(self.name, self.age))
        print(f"Dogs can eat {self.food}")

    def phyPropDog(self):
        print("This dog has " + str(self.numberofLegs) + " legs, while its color is " + self.color + ".")

#inherited from Animal class
class Cats(Animal): #child2

    def __init__(self, name, color, age, ability, numberofLegs = 4):
        super().__init__(name, color, age, numberofLegs)
        print("Cat class is called")
        self.ability = ability

    def meow(self):
        print("Cats make meow sound")

    def propertiesCat(self):
        print("This cat's name is {}, and it's age is {}.".format(self.name, self.age))
        print(f"This cat can do {self.ability}")

    def phyPropCat(self):
        print("This cat has " + str(self.numberofLegs) + " legs, while its color is " + self.color + ".")


c1 = Cats("Lucy", "yellow", 2, "tumbling")
c1.meow()
c1.propertiesCat()
c1.walk()
c1.phyPropCat()
print("------------------------------------------")
d1 = Dogs("Bady", "brown", 3, "meat")
d1.bark()
d1.propertiesDog()
d1.phyPropDog()
print("------------------------------------------")
print("{} animal types are called".format(Animal.counter))

