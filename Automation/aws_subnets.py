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
