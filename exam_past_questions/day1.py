# Write a class named Employee that holds the following data about an employee in
# attributes: name, ID number, department, and job title. The class should provide get and set
# methods for each of the categories as wel as a _ str__ method. Please ensure that al
# attributes remain private to external programs. 


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    # Getter and Setter for Name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for ID Number
    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Getter and Setter for Department
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    # Getter and Setter for Job Title
    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    # String representation
    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"ID Number: {self.__id_number}\n"
                f"Department: {self.__department}\n"
                f"Job Title: {self.__job_title}")



# Employee class

sandra = Employee("Sandra", 12345, "Salon", "Hair Dresser")

print(sandra)

sandra.set_name("JEJE")

print("(***********************")

print(sandra)