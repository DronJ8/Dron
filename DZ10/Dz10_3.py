class DronExp(Exception):
   pass

try:
   n = int(input("Введіть число > 0: "))
   if n < 0:
       raise DronExp(" Ви ввели від'ємне значення!!!: " + str(n))
   print( "Введене користувачем зн є додатнім числом  -  ", n)

except DronExp as e:
  print(e)

