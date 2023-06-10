import os

file_list = []

for name in os.listdir():
    size = os.stat(name).st_size
    
    file_dict = {
        'Name' : name,
        'Size' : size
    }
    
    file_list.append(file_dict)
    
print(file_list)