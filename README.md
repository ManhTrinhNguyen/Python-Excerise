- [Working with List](#Working-with-List)

- [Working with Dictionaries](#Working-with-Dictionaries)

- [Python Program Calculator](#Python-Program-Calculator)

- [OOP And Class](#OOP-And-Class)

   - [Create a Student class](#Create-a-Student-class)
 
   - [Create a Professor class](#Create-a-Professor-class)
 
   - [Create a Lecture class](#Create-a-Lecture-class)
 
   - [Inheritance](#Inheritance)
 
- [Working with Spreadsheets](#Working-with-Spreadsheets) 

## Working with List

**Using the following list:**

`my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]`

**Write a program that prints out all the elements of the list that are higher than or equal to 10:**

I will use for loop to iterate through the List
   
Then I will use `If Else` statement to check if number >= 10 print that number out 

```
for number in my_list: 
  if number >= 10:
    print(number)
```

**Instead of printing the elements one by one, make a new list that has all the elements higher than or equal to 10 from this list in it and print out this new list.**

I will create a new list call `new_list = []` with no element in there
   
Then I will use `for loop` to iterate through the list that provided
   
Then I will use `If Else` statement to check if number >= 10
   
If number >= 10, I will use `append` to add those number to new_list = [] like this : `new_list.append(number)`

```
new_list = []

for number in my_list:
  if number >= 10:
    new_list.append(number)

print(new_list)
```

**Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.**

I will use `input()` to get user input .

I will declare a variable call `user_input = input("")` . This way I can set a value as a Variable .
  
`input()` alway return String but I want integer I can use int(user_input)

I will create a new list to contain those element

I will use `for loop` to iterate through the list

I will use a value that user given then use it to write an If Else Statement to print out a list that contains only those elements are higher than number given by the use
  
Then i will `append` those number into a new list

```
user_input = input("Hey user ! enter a number\n")

new_list_of_user = []

for number in my_list:
  if number > int(user_input):
    new_list_of_user.append(number)

print(new_list_of_user)
```

## Working with Dictionaries

**Using the following dictionary:**

```
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}
```

**Updates the job to Software Engineer**

I will get a dictionary key by using `employee["job"]`
   
Then change a value of it after `=`

```
employee["job"] = "Software Engineer"

print(employee)
```

**Removes the age key from the dictionary**

To remove a key in dictionary Python have a built-in function called pop 

employee.pop("age")

print(employee)

**Loops through the dictionary and prints the key:value pairs one by one**

I will use for loop to through the dictionary and get a key of it 

Then I can print out a key:value pair like this : `print(f"{key}:{employee[key]}")`

```
for key in employee:
  print(f"{key}:{employee[key]}") 
```

## Python Program Calculator

Write a simple calculator program that:

 - takes user input of 2 numbers and operation to execute

 - handles the following operations: plus, minus, multiply, divide

 - does proper user validation and give feedback: only numbers allowed

 - Keeps the Calculator program running until the user types “exit”

 - Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did

!!! Concepts covered: working with different data types, conditionals, type conversion, user input, user input validation

```
# Write a simple calculator program that:

## I will use While loop to write this program . I will let this program run until user want to exit 
## Yes if user want to continues . No If user want to stop
user_input = ""
result = 0
keep_track_times_of_play = []

while user_input != "exit":

  # takes user input of 2 numbers and operation to execute

  ## I will use input() to take use input 
  ## input() return String so I will use int() to convert it into number 

  user_input_1 = input("Put your first number! \n")
  user_input_2 = input("Put your second number! \n")
  
  # handles the following operations: plus, minus, multiply, divide
  ## I will use If else statement to handle operations that user want
  user_input_3 = input("What operator ? \n")
  if user_input_3 == "+":
    result = int(user_input_1) + int(user_input_2)
  elif user_input_3 == "-":
    result = int(user_input_1) - int(user_input_2)
  elif user_input_3 == "*":
    result = int(user_input_1) * int(user_input_2)
  elif user_input_3 == "/":
    result = int(user_input_1) / int(user_input_2)
  else:
    print("Please out a correct Operations !!!")

  ## The result of the calculation would be 
  print(result)

  # Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did
  ## To keep track how many calculations the user has taken I will declare a list on the top call keep_track_times_of_play = []
  ## Everytime user have a new result I will append it to that list

  keep_track_times_of_play.append(result)

  # Keeps the Calculator program running until the user types “exit”
  user_input = input("Do you want to exit ? If yes type exit \n")

  
# Now outside of While loop I have a list of result of the user . I use len() to get a total number of elements inside the list which is how many result that I have inside the list 
print(f"The number of time user play {len(keep_track_times_of_play)}")
```

## OOP And Class 

In the program we need some way to define kind of the `blueprint` for a user, for all the Data and Function.

I want to create a `blueprint` once and I can use the `blueprint` for all of those Data and function

`Blueprint` for a User call `Class` and specific implementation of that `blueprint` is called `Object`

In the Blueprint we don't have any specific value we just have Attribute . Actual value of those Attribute will be then set when we create an `Object` from the `blueprint` . However I need a function that will actually take those specific values and assign them to an object which is created from the blueprint and I will create from the blueprint that function called `def __init__(self)`

`def __init__(self)` called a `constructor`. I have a blueprint and we are construncting object from that blueprint, the constructor function will help us construct objects from the `Class`

`self` is refer to the Class it's in . Help us access and reference all the attribute and functions within that class  

Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects

`def __init__(self, email, name, password, current_job_title):` Those value must be provide to the Constructur whenever I creating a new object

Then now I have to create function in the Class that any User in application can do, any user can change the password or change their job title and logically when change password happen by user, user provides a new password in order to override the old one .

So the flow will be -> Object will be created for that specific user so the initial data for that Object will be provided so we will have the user, email, name, password and current job title

#### Create a Student class

with properties:

 - first name
 - last name
 - age
 - lectures they attend
   
with methods:

 - can print the full name
 - can list the lectures, which the student attends
 - can add new lectures to the lectures list (attend a new lecture)
 - can remove lectures from the lectures list (leave a lecture)

```
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
    if lecture:
      self.lectures.remove(lecture)
    else:
      print("This lecture not exist!!!")


tim = Student("Tim", "Nguyen", 27, ["computer science"])

print(tim.full_name())
print(tim.list_of_lectures())
```

#### Create a Professor class

with properties:

- first name
- last name
- age
- subjects they teach
- with methods:

- can print the full name
- can list the subjects they teach
- can add new subjects to the list
- can remove subjects from the list

```
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
```

### Create a Lecture class

with properties:

- name
- max number of students
- duration
- list of professors giving this lecture
  
with methods:

- printing the name and duration of the lecture
- adding professors to the list of professors giving this lecture

```
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
```

#### Inheritance

As both students and professors have a first name, last name and age, you think of a cleaner solution:

Inheritance allows us to define a class that inherits all the methods and properties from another class.

- Create a Person class, which is the parent class of Student and Professor classes
- This Person class has the following properties: "first_name", "last_name" and "age"
- and following method: "print_name", which can print the full name
- So you don't need the properties and the method in the other two classes. You can easily inherit these.
- Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class

```
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
```

## Working with Spreadsheets

Write a program that:

- reads the provided spreadsheet file `"employees.xlsx"` with the following information/columns: "name", "years of experience", "job title", "date of birth"
  
- creates a new spreadsheet file `"employees_sorted.xlsx"` with following info/columns: `"name"`, `"years of experience"`, where the years of experience is sorted in descending order: so the employee name with the most experience in years is on top.

#### Install package 

Now I want to read  file `"employees.xlsx"` so basically let our Python program read the contents of that file bcs I want to write a logic base on the values that are in this inventory file, I want to calculate stuff


There is a external package that allow me to work with spreadsheets specificly . Much more function and much easier to use . That Package call `openpyxl`


To install `openpyxl`:

 - I need to create Virtual ENV in Python `venv` : `python3 -m venv python-exercise`

 - Activate `venv`: `source python-exercise/bin/activate`

 - Install `openyxl` : `pip install openpyxl`

#### Implementation

`openpyxl.load_workbook()` is a function in order to read my spreadsheet file .




















