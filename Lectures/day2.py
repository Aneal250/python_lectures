# Write a class named Employee that holds the following data about an employee in
# attributes: name, ID number, department, and job title. The class should provide get and set
# methods for each of the categories as wel as a _ str__ method. Please ensure that al
# attributes remain private to external programs. 


# Key things to Know
# what is Class     (done)
# Uses of a class    (done)
# what are Methods   (done)
# what is Encapsulation  (done)
# what are private and protected attributes (done)



# A class is a blueprint for creating objects

# what is an object
# An object is an instance of a class. It is created from a class blueprint and can have its own unique attributes and behaviors.


# Tool that use to create an object, 

# What are Methods
# Methods are functions defined within a class that describe the behaviors of an object. They can access and modify the object's attributes and are called on instances of the class.


# class that hold details, firstName lastName nationality, state of origin and age 

# Arguments   

class Person:
    def __init__(self, first_name, last_name, nationality, state_of_origin, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__nationality = nationality
        self.__state_of_origin = state_of_origin
        self.__age = age

    # Getter and Setter for First Name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Getter and Setter for Last Name
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Getter and Setter for Full Name
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    # Getter and Setter for Nationality
    def get_nationality(self):
        return self.__nationality

    def set_nationality(self, nationality):
        self.__nationality = nationality

    # Getter and Setter for State of Origin
    def get_state_of_origin(self):
        return self.__state_of_origin

    def set_state_of_origin(self, state_of_origin):
        self.__state_of_origin = state_of_origin

    # Getter and Setter for Age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # String representation
    def __str__(self):
        return (f"First Name: {self.__first_name}\n"
                f"Last Name: {self.__last_name}\n"
                f"Nationality: {self.__nationality}\n"
                f"State of Origin: {self.__state_of_origin}\n"
                f"Age: {self.__age}")

# creation of the object emeka
emeka = Person("Emeka", "Anaele", "Nigerian", "Imo", 31)

# print(emeka)

print(emeka.get_first_name())

# full Name
# print(emeka.get_full_name())
