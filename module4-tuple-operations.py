user_data = ('John', 'American', 1964)
print(len(user_data))

if 'American' in user_data:
    print('This person comes from the US!')
    
for element in user_data:
    print(element)
    
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0,1) * 10
print(numbers)


male_names = ['Adam', 'Jerry', 'Tom']

berlin_temp = [13.0, 17.5, 12.0]