grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

print(grades)

grades['Anne'] = 'A'

print(grades)

grades.update({'John':'A'})

print(grades)

print(len(grades))

if 'John' in grades:
    print('John got:', grades['John'])
    
del grades['John']
print(grades)