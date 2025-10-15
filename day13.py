class animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")


class Dog(animal):
    def __init__(self, name, species,breed):
        super().__init__(name, species)
        self.breed = breed
    
    def make_sound(self):
        print("Woof! Woof!")

    animal1 = animal("Generic Animal", "Unknown")
    animal1.make_sound()

dog1 = Dog("Buddy", "Dog", "Labrador")
dog1.make_sound()

print("Name:", dog1.name)
print("Species:", dog1.species)
print("Breed:", dog1.breed)