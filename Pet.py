from unicodedata import name


class Pet:
    """A class describing a pet as extracted from a CSV"""
    def __init__(self, name, species, weight):
        self.pet_name = name
        self.pet_species = species
        self.pet_weight = weight

    def summary(self):
        print(f"This pet's name is: " + self.pet_name)
        print(f"This pet is a: " + self.pet_species)
        print(f"This pet weights: " + str(self.pet_weight) + "kg \n")

    def get_name(self ):
        print(f"The name of this pet is " + self.pet_name)


