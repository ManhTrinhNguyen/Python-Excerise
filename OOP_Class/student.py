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
  
  # print the full name
  def full_name(self):
    print(f"{self.first_name} {self.last_name}")  
  
  # Print the lecture
  def list_of_lectures(self):
    for lecture in self.lectures:
      print(lecture)
  
  # Add new lecture to lecture list
  def add_new_lecture(self, lecture):
    self.lectures.append(lecture)
    
  # Remove lecture from lectures list
  def remove_lecture(self, lecture):
    if lecture in self.lectures:
      self.lectures.remove(lecture)
    else:
      print("This lecture not exist!!!")


tim = Student("Tim", "Nguyen", 27, ["computer science"])

print(tim.full_name())
print(tim.list_of_lectures())