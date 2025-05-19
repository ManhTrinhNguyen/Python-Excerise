
# As both students and professors have a first name, last name and age, you think of a cleaner solution:

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# - Create a Person class, which is the parent class of Student and Professor classes
# - This Person class has the following properties: "first_name", "last_name" and "age"
# - and following method: "print_name", which can print the full name
# - So you don't need the properties and the method in the other two classes. You can easily inherit these.
# - Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class

class Person:
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def full_name(self):
    print(f"{self.first_name} {self.last_name}")


class Student(Person):
  def __init__(self, first_name, last_name, age, lectures):
    super().__init__(first_name, last_name, age)
    self.lectures = lectures

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


class Professor(Person):
  def __init__(self, first_name, last_name, age, subjects):
    super().__init__(first_name, last_name, age)
    self.subjects = subjects
  
  # Print full name
  def full_name(self):
    print(f"{self.first_name} {self.last_name}")

  # Print the subject Professor teac
  def list_of_subjects(self):
    for subject in self.subjects:
      print(subject)

  # Add new subject to subjects list
  def add_new_subject(self, subject):
    self.subjects.append(subject)
    
  # Remove lecture from lectures list
  def remove_subject(self, subject):
    if subject in self.subjects:
      self.subjects.remove(subject)
    else:
      print(f"This subject {subject} is not exist!!!")