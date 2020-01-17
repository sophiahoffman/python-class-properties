from student import Student
from patient import Patient

new_student = Student()
new_student.first_name = "John"
new_student.last_name = "Doe"
new_student.cohort_number = 36
new_student.age = 42
# new_student.full_name = "Happy Days"
print(new_student)

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way")


# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)
# "097-23-1003"

# # These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# # But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"








