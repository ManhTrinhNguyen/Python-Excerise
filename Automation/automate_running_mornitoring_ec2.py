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



