with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        try:
            number_1 = int(f.readline())
            number_2 = int(f.readline())
            number_3 = int(f.readline())
            result = number_1 / number_2 + number_3
            f_1.write(str(result))
        except ValueError:
            f_1.write('data error')
        except ZeroDivisionError:
            f_1.write('division by 0')
