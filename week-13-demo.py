import os

file_list = []  # Create an empty list to store file information

for name in os.listdir():  # Iterate over the files in the current directory
    size = os.stat(name).st_size  # Get the size of the current file
    
    file_dict = {  # Create a dictionary to store file name and size
        'Name' : name,
        'Size' : size
    }
    
    file_list.append(file_dict)  # Add the dictionary to the file_list
    
print(file_list)  # Print the list containing file information
