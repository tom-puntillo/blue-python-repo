grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for el in grades:
    print(el)
    
for el in grades.keys():
    print(el)
    
for el in grades.values():
    print(el)
    
for person, grade in grades.items():
    print(person, 'got', grade)