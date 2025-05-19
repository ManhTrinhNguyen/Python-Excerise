class Professor:
  def __init__(self, first_name, last_name, age, subjects):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
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

kelly = Professor("Kelly", "Le", 23, ["Dentist"])

print(kelly.full_name())