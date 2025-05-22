- [Working with List](#Working-with-List)

- [Working with Dictionaries](#Working-with-Dictionaries)

- [Python Program Calculator](#Python-Program-Calculator)

- [OOP And Class](#OOP-And-Class)

   - [Create a Student class](#Create-a-Student-class)
 
   - [Create a Professor class](#Create-a-Professor-class)
 
   - [Create a Lecture class](#Create-a-Lecture-class)
 
   - [Inheritance](#Inheritance)
 
- [Working with Spreadsheets](#Working-with-Spreadsheets)

- [Python Automation](#Python-Automation)

   - [Working with Subnets in AWS](#Working-with-Subnets-in-AWS)
 
   - [Boto3 Configuration](#Boto3-Configuration)
 
   - [Working with IAM in AWS](#Working-with-IAM-in-AWS)
 
   - [ Automate Running and Monitoring Application on EC2 instance](#Automate-Running-and-Monitoring-Application-on-EC2-instance)


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

## Python Automation 

I want to use Python to talk to external Application 

!!! NOTE : Communication between 2 Applications, in this case Python Application and AWS usually happens using a HTTP Protocol .

Python has a library called `Boto3` that makes it possible to work with `AWS resources` .

- I can create resources, configure resources fetch the data about them and do all sorts operations on my AWS account

To install Boto3: `pip install boto3` (Make sure to create VENV first) 

Boto3 Documents : (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

####  Boto3 Configuration

Just like we did with Terraform I want to connect to AWS account and authenticate with our `AWS User` .

We can configure using AWS configure command if I have aws CLI installed locally, which sets four values (aws_access_id, aws_access_secret_key, region, output format)

`Boto3` will automatically take these credentiasl and the default region information to connect to AWS and authenticate with it . That mean I do not need to do anything

My AWS credentials live here : `ls ~/.aws`

### Working with Subnets in AWS

In this task a I will:

- Get all the subnets in your default region

- Print the subnet Ids

**Get all the subnets in your default region**

First i need to import boto3 `import boto3`

Basically in Boto3 I have a `Client` for EC2 that will be able to connect to AWS and do something for EC2 related components . And that is why we gonna create a Client from EC2 :` client = boto3.client('ec2')`

To get all the subnets in my default region I will use `describe_subnets` in my `EC2 Client` (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_subnets.html)

```
import boto3

client = boto3.client('ec2')

# Get all the subnets in your default region and print out all subnets id 

response = client.describe_subnets()

# I will iterate through to Subnet list and get the subnet ID 
# I can also create a list and append all the subnet id into it 

subnets_id_list = []

for subnet in response['Subnets']:
  subnets_id_list.append(subnet["SubnetId"])

print(subnets_id_list)
```

### Working with IAM in AWS 

This document is use to work with IAM (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#client)

I also have a `Client` IAM . 

```
# Import the boto3 library to interact with AWS services
import boto3

# Create an IAM client using boto3
client = boto3.client('iam')

# List all IAM users in the AWS account
response = client.list_users()

# Initialize an empty list to store users who have logged in before
new_user_list = []

# Iterate through each user in the list
for user in response['Users']:

  # For each user, print out the name of the user and when they were last active (hint: Password Last Used attribute)
  print(f"UserName: {user["UserName"]}")
  print(f"Last Active: {user.get('PasswordLastUsed', 'Never used')}")


  # Check if the user has ever logged in (i.e., has 'PasswordLastUsed' attribute)
  if "PasswordLastUsed" in user:
      # Add user to the list of users who have logged in
      new_user_list.append(user)

# If the list is not empty, find the most recently active user
if new_user_list:
    # Use max() to find the user with the most recent 'PasswordLastUsed' timestamp
    most_recent_user = max(new_user_list, key=lambda u: u['PasswordLastUsed'])

    # Print the username of the most recently active user
    print(f"Most recently active user: {most_recent_user['UserName']}")
else:
    print("No users have logged in.")

   
```

#### AWS IAM User Activity Tracker Python and Boto3

This Python script uses the **Boto3** AWS SDK to list IAM users in your AWS account and determine **who was the most recently active user** based on the `PasswordLastUsed` attribute.

#### Features

- Lists all IAM users in your account.
- Filters only those users who have logged in at least once.
- Identifies and prints the **most recently active IAM user**.

#### Requirements

- Python 3.x
- `boto3` package
- AWS credentials configured via:
  - `~/.aws/credentials`
  - or environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)

Install dependencies: `pip install boto3`

#### Code Explanation

Uses `boto3.client('iam')` to interact with IAM.

Calls `list_users()` to fetch all IAM users.

Filters users who have the `PasswordLastUsed` field.

Finds the most recently active user using `max()` and `lambda`.

Prints out that user’s name.

##  Automate Running and Monitoring Application on EC2 instance

```
import boto3
import paramiko 
import time
import schedule
import requests
from botocore.exceptions import ClientError



client = boto3.client('ec2')

# Write a Python program which automatically creates an EC2 instance, 
# Installs Docker inside and starts an Nginx application as Docker container and starts monitoring the application as a scheduled task. 
# Write the program with the following steps:

# All needed variable values 
image_id = 'ami-07706bb32254a7fe5'
instance_type = 't3.medium'
key_name = 'terraform'

# the pem file must have restricted 400 permissions: chmod 400 absolute-path/boto3-server-key.pem
ssh_private_key_path = '/Users/trinhnguyen/.ssh/terraform.pem'
ssh_user = 'ec2_user'

# Check EC2 instance that exist or not 
describe_instance = client.describe_instances(
  Filters=[
    {
      'Name': 'tag:Name',
      'Values': [
        'python-server-16'
      ]
    }
  ]
) 

# Instance already existed
instance_already_existed = len(describe_instance['Reservations']) != 0 and len(describe_instance['Reservations'][0]["Instances"]) != 0
instance_id = ''

# If EC2 Instance exist print that instance 
if not instance_already_existed: 
  # If instance doesn't exist yet . Create a new EC2 Instance 
  print("Instances not exist create new one")
  create_ec2_instance = client.run_instances(
    ImageId = 'ami-07706bb32254a7fe5',
    InstanceType = 't3.medium',
    KeyName = 'terraform',
    MinCount = 1,
    MaxCount = 1,
    SecurityGroupIds = ['sg-00b8ccb65c3b173e0'],
    TagSpecifications = [
      {
        'ResourceType': 'instance',
        'Tags': [
          {
            'Key': 'Name',
            'Value': 'python-server-16'
          }
        ]
      }
    ]
  )
  instance_id = create_ec2_instance['Instances'][0]['InstanceId']
else:
   print('This instance already exist')
   print(describe_instance['Reservations'][0]["Instances"][0])


# Wait until the EC2 server is fully initialized

print('Wait for instance is initilazing for 90s')
time.sleep(90)

is_instances_initialized = False 

while is_instances_initialized == False:
   describe_status = client.describe_instance_status(
      InstanceIds = [instance_id],
   )['InstanceStatuses'][0]

   instance_status = describe_status['InstanceStatus']['Status']

   if instance_status != 'ok':
    print(instance_status)

   if instance_status == 'ok':
      print(f"Instance status is {instance_status} now !!!!")
      print('EC2 server is fully initialized')
      break
   

# Install Docker on the EC2 server

describe_instance = client.describe_instances(
  Filters=[
    {
      'Name': 'tag:Name',
      'Values': [
        'python-server-16'
      ]
    }
  ]
)

instance = describe_instance["Reservations"][0]["Instances"][0]
ssh_host = instance["PublicIpAddress"]

print(f"EC2 Server Public IP Address {ssh_host}")
security_group_id = instance['SecurityGroups'][0]['GroupId']


cmd_install_docker = """
sudo yum update -y 
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo docker run -d -p 8080:80 --name nginx nginx
"""



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
  ssh.connect(hostname=ssh_host ,username='ec2-user', key_filename=ssh_private_key_path)

  stdin, stdout, stderr = ssh.exec_command(cmd_install_docker)
  output = stdout.readlines()
  print(output)

  # print any error 
  error_output = stderr.read().decode()
  if error_output:
    print("Error output")
    print(error_output)

  # Close streams explicitly
  stdout.channel.close()
  stderr.channel.close()
  stdin.close()
finally:
  ssh.close()

# Open port for nginx to be accessible from browser

try:
  security_group_ingress = client.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
      {
        'IpProtocol': 'tcp',
        'FromPort': 8080,
        'ToPort': 8080,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
      }
    ]
  )
except ClientError as e:
  if 'InvalidPermission.Duplicate' in str(e):
        print("Port 8080 is already open.")
  else:
      raise  


# Create a scheduled function that sends a request to the nginx application and checks the status is OK

print("Wait 30s for Nigix running")

time.sleep(30)

def send_request_to_nginx():
  max_tries = 5

  for attempt in range(1, max_tries + 1):
    try:
      r = requests.get(f"http://{ssh_host}:8080", timeout=5)
      status_code = r.status_code
      print(f"Application is up !!! Status Code: {status_code}")
      break
    except requests.exceptions.RequestException as e:
        print("Something went wrong with the application.")
        print(f"Attempt {attempt} failed {e}")
        if attempt < max_tries:
           time.sleep(3)
        else: 
           print("❗App failed to respond after 5 attempts.")
           print("Restart Nginx")

           ssh = paramiko.SSHClient()
           ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           try:
            ssh.connect(hostname=ssh_host ,username='ec2-user', key_filename=ssh_private_key_path)
            restart_cmd = """
              sudo docker rm -f nginx || true
              sudo docker run -d -p 8080:80 --name nginx nginx
            """
            stdin, stdout, stderr = ssh.exec_command(restart_cmd)
            output = stdout.readlines()
            print(output)

            # print any error 
            error_output = stderr.read().decode()
            if error_output:
              print("Error output")
              print(error_output)

            # Close streams explicitly
            stdout.channel.close()
            stderr.channel.close()
            stdin.close()
           finally:
            ssh.close()
           

schedule.every(10).seconds.do(send_request_to_nginx)

while True:
  schedule.run_pending()
```

#### EC2 Auto-Deploy & Monitor Nginx with Docker using Python (Boto3 + Paramiko)

This Python script automates the full lifecycle of deploying an Nginx Docker container on an AWS EC2 instance.

#### Features

- 🚀 Creates a new EC2 instance (if not already present)
- 🐳 Installs Docker and runs an Nginx container
- 🔐 Opens port `8080` via Security Group for external access
- 📡 Monitors the Nginx application every 10 seconds
- 🔁 Automatically restarts the Nginx container if it becomes unreachable

---

#### Requirements

- Python 3.8+
- AWS credentials configured (`~/.aws/credentials` or via environment variables)
- A `.pem` key file with permission `chmod 400`
- Pre-created security group that allows port 8080 (or allow it via script)

#### Python Packages

Install dependencies using `pip`: `pip install boto3 paramiko requests schedule`

#### Configuration

```
image_id = 'ami-07706bb32254a7fe5'       # Amazon Linux 2 AMI
instance_type = 't3.medium'
key_name = 'terraform'                   # EC2 key pair name
ssh_private_key_path = '/path/to/terraform.pem'
ssh_user = 'ec2-user'
tag_name = 'python-server-16'
security_group_id = 'sg-xxxxxxxxxxxxxxx' # Pre-created SG or allow via script
```

#### What it does:

Checks if an EC2 instance with tag python-server-16 exists.

If not, it creates one and waits for it to be ready.

Connects via SSH to install Docker and launch Nginx in a container.

Opens port 8080 in the Security Group.

Monitors the Nginx application every 10 seconds.

If the app fails 5 times in a row, it will restart the Docker container.





