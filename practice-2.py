import random

instances_needed = int(input('How many EC2 Instances do you need? '))
department_name = input('What department are you in? ')

if department_name == 'Marketing' or department_name == 'Accounting' or department_name == 'FinOps':
    print('Here are the names of your EC2 instances: ')
    
    for n in range(instances_needed):
        print(department_name, random.randrange(instances_needed), random.randrange(instances_needed), sep='_')

else:
    print('You should not be using this name genterator')