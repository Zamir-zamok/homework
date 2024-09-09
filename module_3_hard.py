def data_structure(chislo):
    summa = 0
    for i in chislo:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            summa += data_structure(i)
        elif isinstance(i, dict):
            summa += data_structure(i.values())
            summa += data_structure(i.keys())
    return summa
data_structura = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(data_structure(data_structura))