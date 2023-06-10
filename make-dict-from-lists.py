import os
files = {}
file_list = os.listdir()
file_name_list = []
file_size_list = []

for name in file_list:
    if name in file_list:
        file_name_list.append(name)

for size in file_list:
    file_size_list.append((os.stat((size)).st_size))

for i in range(len(file_name_list)):
    files[file_name_list[i]] = file_size_list[i]


for name, size in files.items():
    print(name, ':', size)