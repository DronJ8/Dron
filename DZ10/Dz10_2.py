
def A1(sl):
    if len(set(sl)) == len(sl):
        return "всі числа унікальні"
    else:
        return "не всі числа унікальні"
ss= [1,2,3,3,4]


def F2 (sl2):
    try:
        return A1(sl2)
    except NameError as nerr:
        print("виникла помилка 1", nerr)
    except TypeError as terr:
        print("виникла помилка 2", terr)

print(F2(ss))
