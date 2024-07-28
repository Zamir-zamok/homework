immutable_var = (1, 2, 'a', 'true')
print(immutable_var) # изменить элементы нельзя, так как кортеж это неизменяемая упорядоченная коллекция
mutable_list = [1, 3, 5, 'c']
mutable_list.append(589)
print(mutable_list)