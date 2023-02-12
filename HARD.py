N = int(input('Если пространство двухмерное - введите 2, если трехмерное - 3'))

list_a =[]
list_b =[]

for a in range(N):
    list_a.append((int(input(f'введите кординату точки А №{a+1}'))))

print(list_a)

for b in range(N):
    list_b.append((int(input(f'введите кординату точки B №{b+1}'))))

print(list_b)


sum_1 = 0
sum_2 = 0

for i in range(N):
    sum_1 = (list_b[i] - list_a[i])**2
    sum_2 += sum_1

lenght = sum_2**0.5

print(lenght)