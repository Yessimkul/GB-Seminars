# Это математика :
# Теорема Виета - буду решать через Дискриминант
#S = a + b; S = P/b + b; S - b = P/b; P= Sb-b**2; b**2 - Sb + P ==0;
#P = a * b; a = P/b;

# import math
#
S = int(input('Введите сумму'))
P = int(input('Произведение'))
# if S and P <= 1000:
#     discr = S ** 2 - 4 * P
#     print(f"Дискриминант D = {discr}")
#
#     if discr > 0:
#         x1 = (S + math.sqrt(discr)) / 2
#         x2 = (S - math.sqrt(discr)) / 2
#         if x1+x2 == S:
#             print(f'a = {int(x1)}; b = {int(x2)}')
#         else:
#             print("неправильно введены данные")
#     elif discr == 0:
#         x = S / 2
#         print(f" а и b = {int(x)}")
#     else:
#         print("нет таких натуральных чисел")
# else:
#     print("Вы вышли за пределы задаваемых значений")


# Или вложенным циклом ?

for a in range(1000):
    for b in range(1000):
        if a + b == S and a*b == P:
            print(f' a = {a}, b = {b}')



