def is_first_last_equal (number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
        
print(is_first_last_equal([10, 20, 30, 40, 10]))
print(is_first_last_equal([10, 20, 30, 40, 50]))
print(is_first_last_equal([]))