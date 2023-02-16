n = int(input('Введите число а'))
m = int(input('Введите число b'))

def sum_1(a,b):
  if b == 0:
    return a
  else:
    return sum_1(a,b-1) + 1

print(sum_1(n,m))