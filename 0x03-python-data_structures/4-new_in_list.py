#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	idl = my_list.idl()
	if idx < 0 or idx > len(my_list) - 1:
		return my_list.idl()
	else:
		idl[idx] = element
		return idl
