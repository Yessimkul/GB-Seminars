from random import randint

a = []

n = int(input('Введите количество монет'))

for i in range(n):
    a.append(randint(0, 1))
print(a)
# заполняем лист значениями от 0 до 1
counter = 0

for e in range(len(a)):
    if a[e] == 0:
        counter +=1
# Считаем сколько необходимо перевернуть

print(f'Нужно перевернуть {counter} монет из  {n}')