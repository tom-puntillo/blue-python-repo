import os

path = "."

for root, d_names, f_names in os.walk(path):
   print(root, d_names, f_names)