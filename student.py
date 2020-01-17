# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

class Student:
    @property
    def first_name (self):
        return self.__first_name

    @property
    def last_name (self):
        return self.__last_name

    @property
    def age (self):
        return self.__age

    @property
    def cohort_number (self):
        return self.__cohort_number
    
    @property
    def full_name (self):
        if (self.__first_name != "" and self.__last_name != ""):
            self.__full_name = self.__first_name + " " + self.__last_name
            return self.__full_name
        else:
            return "No full name"

    @first_name.setter
    def first_name (self, first_name):
        self.__first_name = first_name
    
    @last_name.setter
    def last_name (self, last_name):
        self.__last_name = last_name
    
    @age.setter
    def age (self, age):
        if type(age) is int:
            self.__age  = age 
        else:
            raise TypeError('Please provide an integer value for age')
    
    @cohort_number.setter
    def cohort_number (self, cohort_number):
        if type(cohort_number) is int:        
            self.__cohort_number = cohort_number
        else:
            raise TypeError('Please provide an integer value for age')

    def __str__ (self):
        return f"{self.full_name} is {str(self.__age)} years old and is in cohort {self.__cohort_number}."
