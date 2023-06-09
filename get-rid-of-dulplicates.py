def unique(my_list = []):
    my_other_list = []
    for n in my_list:
        if n not in my_other_list:
            my_other_list.append(n)
    return my_other_list
        
print(unique([1, 2, 5, 1, 6, 1, 9, 5, 1, 6, 3]))
