- [Working with List](#Working-with-List)

## Working with List

**Write a program that prints out all the elements of the list that are higher than or equal to 10:**

 - I will use for loop to iterate through the List
   
 - Then I will use `If Else` statement to check if number >= 10 print that number out 

```
for number in my_list: 
  if number >= 10:
    print(number)
```

**Instead of printing the elements one by one, make a new list that has all the elements higher than or equal to 10 from this list in it and print out this new list.**

 - I will create a new list call `new_list = []` with no element in there
   
 - Then I will use `for loop` to iterate through the list that provided
   
 - Then I will use `If Else` statement to check if number >= 10
   
 - If number >= 10, I will use `append` to add those number to new_list = [] like this : `new_list.append(number)`

```
new_list = []

for number in my_list:
  if number >= 10:
    new_list.append(number)

print(new_list)
```

**Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.**

- I will use `input()` to get user input .

- I will declare a variable call `user_input = input("")` . This way I can set a value as a Variable .
  
- `input()` alway return String but I want integer I can use int(user_input)

- I will create a new list to contain those element

- I will use `for loop` to iterate through the list

- I will use a value that user given then use it to write an If Else Statement to print out a list that contains only those elements are higher than number given by the use
  
- Then i will `append` those number into a new list

```
user_input = input("Hey user ! enter a number\n")

new_list_of_user = []

for number in my_list:
  if number > int(user_input):
    new_list_of_user.append(number)

print(new_list_of_user)
```




