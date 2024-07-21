my_dict = {'Zamir':1993, 'Sabina':1995, 'Ded':2001}
print(my_dict)
print(my_dict['Zamir'])
print(my_dict.get ('Gleb'))
my_dict.update({'Masha':1995,
                'Sveta':1996})
a = my_dict.pop('Ded')
print(a)
print(my_dict)

my_set = {1,2,3,3,4,4,'tablo'}
print(my_set)
my_set.add(5)
my_set.add('tupak')
my_set.discard(4)
print(my_set)