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