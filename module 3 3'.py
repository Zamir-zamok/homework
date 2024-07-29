def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list=['@', 'False', 99]
values_dict={'a':1993, 'b':2001,'c':1972}
values_list_2=[10,41]

print_params(2)
print_params(2, 4)
print_params(False, 'z', 10)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 42)