name_original = 'Jodi'
name_new = name_original
name_original  = 'Tommy'
print(name_original, name_new)


list_original = [1,2,3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)


list_original = [1,2,3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)


list_original = [1,2,3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)