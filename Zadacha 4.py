# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько
# журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#

# S - общее количество журавликов
# Петя и Сераже сделали каждый по "а" журавликов, занчит Катя сделала "2*(а+а)" журавликов
# Соответственно общее количество == а + а + 2* 2а == 6а
# значит а == S//6

s = int(input('введите общее количество яблок которое собрали дети'))

if s%6 != 0:
    print('невозможно собрать нецелые яблоки с деревьев')
else:
    a = s/6
    print(f'Из {s} яблок Катя собрала {a*4}, а Петя и Сережа каждый по {a} ')