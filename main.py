a = int (input("Введіть значення А"))
b = int (input("Введіть значення Б"))
def mane_function (a1, b1):
    if a1 > b1:
        return a1
    else:
        return b1
print("Більше число - ", mane_function(a, b))