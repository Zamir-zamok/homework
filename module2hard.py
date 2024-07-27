def funk(n):
    list1 = ""
    if n >=3:
        for j in range(1, n):
            for m in range(j+1, n):
                if n % (j+m) == 0:
                    txt = (str(j)+str(m))
                    list1 += "".join(txt)
    return (f"{n} - {list1}")

n = int(input("Введите число от 3 до 20 "))
print(funk(n))