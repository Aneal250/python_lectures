# (a) Write a class, named Pet, which should have the following data attributes:
# - _ name
# __animal_type
# __age
# (for the name of a pet)
# (for the type of animal that a pet is. Example values are 'Dog',
# 'Cat', and 'Bird')
# (for the pet's age) (8 Marks)
# (b) The Pet class should have an __init__ method that creates these attributes. It
# should also have the following methods:
# set_name
# set_animal_type
# This method assigns a value to the __name field.
# This method assigns a value to the __ animal_type field.
# set_age
# This method assigns a value to the __ age field.
# get_name
# This method returns the value of the __ name field.
# get_animal_type
# get_age
# This method returns the value of the __ animal_type field.
# This method returns the value of the __ age field.
# (c) Once you have written the class, write a program that creates an object of the class
# and prompts the user to enter the name, type, and age of his or her pet. This data
# should be stored as the object's attributes. Use the object's accessor methods to
# retrieve the pet's name, type, and age and display this data on the screen.
# (12 Marks)
# (1

# create a class Name of Pets
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age


    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
    def __str__(self):
        return f"Pet Name: {self.__name}, Type: {self.__animal_type}, Age: {self.__age}"
    
    
# (c) Once you have written the class, write a program that creates an object of the class
# and prompts the user to enter the name, type, and age of his or her pet. This data
# should be stored as the object's attributes. Use the object's accessor methods to
# retrieve the pet's name, type, and age and display this data on the screen. 

def main():
    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of your pet (Dog, Cat, Bird): ")
    age = int(input("Enter the age of your pet: "))

    pet = Pet(name, animal_type, age)

    print("\nPet Information:")
    print(f"Name: {pet.get_name()}")
    print(f"Type: {pet.get_animal_type()}")
    print(f"Age: {pet.get_age()}")

if __name__ == "__main__":
    main()