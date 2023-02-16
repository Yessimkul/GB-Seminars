a = int(input("введите число, которое будем возводить в степень"))
n = int(input("введите число - степень"))

def sqrt_1(b):
  if b == 1:
    return a
  return  a * sqrt_1(b-1)

print(sqrt_1(n))