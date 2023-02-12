# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы

one_lat = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
two_lat = ['D', 'G']
three_lat = ['B', 'C', 'M', 'P']
four_lat = ['F', 'H', 'V', 'W', 'Y']
five_lat = ['K']
eight_lat = ['J', 'X']
ten_lat = ['Q', 'Z']

one_kir = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_kir = ['Д', 'К', 'Л', 'М', 'П', 'У']
three_kir = ['Б', 'Г', 'Ё', 'Ь', 'Я']
four_kir = ['Й', 'Ы']
five_kir = ['Ж', 'З', 'Х', 'Ц', 'Ч']
eight_kir = ['Ш', 'Э', 'Ю']
ten_kir = ['Ф', 'Щ', 'Ъ']

word = str(input('введите слово'))
a = word.upper()
counter = 0

for i in range(len(a)):
    if a[i] in one_lat:
        counter +=1
    elif a[i] in two_lat:
        counter +=2
    elif a[i] in three_lat:
        counter +=3
    elif a[i] in four_lat:
        counter +=4
    elif a[i] in five_lat:
        counter +=5
    elif a[i] in eight_lat:
        counter +=8
    elif a[i] in ten_lat:
        counter +=10
    else:
        if a[i] in one_kir:
            counter += 1
        elif a[i] in two_kir:
            counter += 2
        elif a[i] in three_kir:
            counter += 3
        elif a[i] in four_kir:
            counter += 4
        elif a[i] in five_kir:
            counter += 5
        elif a[i] in eight_kir:
            counter += 8
        elif a[i] in ten_kir:
            counter += 10

print(counter)
