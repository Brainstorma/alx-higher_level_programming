#!/usr/bin/python3
# Program to print numbers from 0 to 98 in decimal and hexadecimal
print('Number\t\tDecimal\t\tHexadecimal')

for fun in range(0, 99): 
    print('{}\t\t{}\t\t{}'.format(fun, fun, hex(fun)))
