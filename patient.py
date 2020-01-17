# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.

class Patient():
    def __init__ (self, ssn, dob, insurance_account, first_name, last_name, address):
        self.__social_security_number=ssn
        self.__date_of_birth = dob
        self.__insurance_account = insurance_account
        self.__full_name = first_name + " " + last_name
        self.__address = address

    @property
    def social_security_number (self):
        return self.__social_security_number

    @property
    def date_of_birth (self):
        return self.__date_of_birth

    @property
    def insurance_account (self):
        return self.__insurance_account
    
    @property
    def full_name (self):
        return self.__full_name

    @property
    def address (self):
        return self.__address
        
    @address.setter
    def address (self, address):
        self.__address = address
        return self.__address

    def __str__ (self):
        return (self.full_name)






