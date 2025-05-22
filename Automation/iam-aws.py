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

   
 