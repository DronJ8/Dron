a = int (input("Введіть зн A"))
b = int (input("Введіть зн Б"))
def mane_function (a1, b1):
    if a1 > b1:
        return a1
    else:
        return b1
print("Більше число - ", mane_function(a, b))
print("Квадрат числа - ", mane_function(a, b) * mane_function(a, b))


def test_funcktion( b1, c1, d1):
    if b1 > c1 and d1 > b1:
        print("Умови виконуються")

b = 6
c = 4
d = 64
test_funcktion(b, c, d)

