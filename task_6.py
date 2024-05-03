with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        try:
            number = int(f.readline())
            count = 0
            for line in f:
                count += 1
            if number == count:
                f_1.write('YES')
            else:
                f_1.write('NO')
        except ValueError:
            f_1.write('ERROR')
