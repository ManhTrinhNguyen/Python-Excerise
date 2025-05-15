- [Working with List](#Working-with-List)

- [Working with Dictionaries](#Working-with-Dictionaries)

- [Python Program Calculator](#Python-Program-Calculator)

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













