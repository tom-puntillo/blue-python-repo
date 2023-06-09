import os

path = '/home/ec2-user/environment/blue-python-repo'

path1 = '/home/ec2-user/environment/'

print(os.getcwd())

print(os.listdir())

print(os.stat(('/home/ec2-user/environment/.c9')).st_size)
