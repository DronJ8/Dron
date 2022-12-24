a = int (input("Введіть зн A"))
b = int (input("Введіть зн Б"))
def mane_function (a1, b1):
    if a1 > b1:
        return a1
    else:
        return b1
print("Більше число - ", mane_function(a, b))
print("Квадрат числа - ", mane_function(a, b) * mane_function(a, b))