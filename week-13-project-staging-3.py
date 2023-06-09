import os

os.chdir('/home/ec2-user/environment/blue-python-repo')

files = {}

file_list = os.listdir()

file_name_list = []
file_size_list = []

name = ''
size = ''

for name in file_list:
    for size in file_list: