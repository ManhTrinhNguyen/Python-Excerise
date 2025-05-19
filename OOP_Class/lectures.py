# with properties:

# - name
# - max number of students
# - duration
# - list of professors giving this lecture
  

class Lecture:
  def __init__(self, name, max_number_students, duration, professors_on_this_lecture):
    self.name = name
    self.max_number_students =  max_number_students
    self.duration = duration
    self.professors_on_this_lecture = professors_on_this_lecture
  
  # printing the name and duration of the lecture
  def name_and_duration(self):
    print(f"{self.name}")
    print(f"{self.duration}")

  # adding professors to the list of professors giving this lecture
  def add_professor_to_lecture(self, professor):
    if professor not in self.professors_on_this_lecture:
      self.professors_on_this_lecture.append(professor)
      print(self.professors_on_this_lecture)
    else:
      print(f"This Professor {professor} is already in the list")


computer = Lecture("computer science", 24, 100, ["Tim", "Kelly"])

print(computer.add_professor_to_lecture("Kelly"))