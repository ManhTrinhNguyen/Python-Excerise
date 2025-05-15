# Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects:

# a) Create a Student class:

# with properties:

#  - first name
#  - last name
#  - age
#  - lectures they attend
   
# with methods:

#  - can print the full name
#  - can list the lectures, which the student attends
#  - can add new lectures to the lectures list (attend a new lecture)
#  - can remove lectures from the lectures list (leave a lecture)

class Student:
  def __init__(self, first_name, last_name, age, lectures):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age 
    self.lectures = lectures
  
  def full_name(self):
    print(f"{self.first_name} {self.last_name}")
  
  def list_of_lectures(self):
    list_of_lectures = []
    list_of_lectures.append(self.lectures)
    

