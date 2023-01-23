#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                new_list.append(my_list_1[i] / my_list_2[i])
            else:
                print("wrong type")
                new_list.append(0)
        except (IndexError, ZeroDivisionError):
            if isinstance(my_list_2[i], int) and my_list_2[i] == 0:
                print("division by 0")
            else:
                print("out of range")
            new_list.append(0)
    return new_list
