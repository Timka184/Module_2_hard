n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('Список:', *n)
number = int(input('Введите число из списка: '))
if number not in n:
    print('Число не из списка!')
else:
    found_pairs = set()
    for i in m:
        for j in m:
            if i != j:
                total = i + j
                if number % total == 0:
                    found_pairs.add(tuple(sorted((i, j))))
    found_pairs = sorted(found_pairs)
    if found_pairs:
        result = ''.join(f'{pair[0]}{pair[1]}' for pair in found_pairs)
        print('Пароль:', result)
