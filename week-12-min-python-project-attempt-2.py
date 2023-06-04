import random

instances_needed = int(input('How many EC2 Instances do you need? '))
department_name = input('What department are you in? ')

for n in range(instances_needed):
    print(department_name, random.randrange(instances_needed), random.randrange(instances_needed), sep='_')