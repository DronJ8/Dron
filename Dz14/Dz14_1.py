import  random
import time
from random_word import RandomWords

w=RandomWords()


int_list = []
float_list = []
str_list = []

for i in range (50):
    int_list.append(random.randint(1,100))
for j in range (50):
    float_list.append(random.uniform(0.1, 100))
for ij in range (50):
    str_list.append(w.get_random_word())


print("Словник з випадковими цілими числами", int_list)
print("Словник з випадковими дробовими числами", float_list)
print("Словник з випадковими словами", str_list)

def F1 (data):
    ind = 0
    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
            ind += 1
        data[minIndex] = tmp
    print("Відсортований список:", data)
    print("кількість ітерацій", ind)

cur_time = time.time()
F1(int_list)
temp_time = time.time()
print("Час сортування:", temp_time - cur_time)