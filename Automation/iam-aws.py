import boto3

client = boto3.client('iam')

# Get all the IAM users in your AWS account
response = client.list_users()

## I will iterate through the user list
for user in response['Users']:

# For each user, print out the name of the user and when they were last active (hint: Password Last Used attribute)
  # print(f"UserName: {user["UserName"]}")
  # print(f"Last Active: {user.get('PasswordLastUsed', 'Never used')}")
  
# Print out the user ID and name of the user who was active the most recently
## First I will create new user list 
  new_user_list = []
## Check if PasswordLastUsed in user 
  if "PasswordLastUsed" in user:
    ## I will append user that have PasswordLastUsed to new user list
    new_user_list.append(user)
    ## Then I will sort the PasswordLastUsed descending to get the most recent user
    most_recent_user = max(new_user_list, key=lambda u: u['PasswordLastUsed'])
    ## Then now I will print out the most recent user name
    print(most_recent_user["UserName"])

   
  
