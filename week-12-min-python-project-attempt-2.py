import random

ec2list = []

instances_needed = int(input('How many EC2 Instances do you need? '))
department_name = input('What department are you in? ')

for n in range(instances_needed):
    r = random.randint(1,instances_needed)
    if r not in ec2list:
        ec2list.append(r)
        
    print(department_name,'-', r)