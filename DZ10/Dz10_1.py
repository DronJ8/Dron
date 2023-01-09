def Monat(num):
    month = {1: 'січень',
             2: 'лютий',
             3: 'березень',
             4: 'квітень',
             5: 'травень',
             6: 'червень',
             7: 'липень',
             8: 'серпень',
             9: 'вересень',
             10: 'жовтень',
             11: 'листопад',
             12: 'грудень',
             }
    try:
        return month[num]
    except KeyError as kerr:
        print(kerr, "введіть натуральне число з діапазону 1-12")
    except TypeError as tperr:
        print(tperr, "введіть коректне значення")
    except NameError as nerr:
        print(nerr, "введіть коректне значення1")

m = Monat([1,2,3])
print(m)