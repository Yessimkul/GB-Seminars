
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

from random import randint

N = int(input('введите количество чисел в массиве'))

lst = [randint(1,15) for _ in range(N)]
print(lst)

x = int(input("введите число, которое должно быть посчитано в списке"))
counter = 0

for i in range(len(lst)):
  if x == lst[i]:
    counter +=1

print(f'число {x} встречается {counter} раз')