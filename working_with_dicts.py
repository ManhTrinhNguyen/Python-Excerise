# Using the following dictionary:

employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Updates the job to Software Engineer

## I will get a dictionary key by using employee["job"] 
## Then change a value of it after = 

employee["job"] = "Software Engineer"

print(employee)

# Removes the age key from the dictionary 

## To remove a key in dictionary Python have a built-in function called pop 

employee.pop("age")

print(employee)

# Loops through the dictionary and prints the key:value pairs one by one 

## I will use for loop to through the dictionary and get a key of it  
## Then I can print out a key:value pair like this : print(f"{key}:{employee[key]}") 

for key in employee:
  print(f"{key}:{employee[key]}") 




