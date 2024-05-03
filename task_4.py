with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        for line in f:
            if len(line) - 1 > 20:
                f_1.write(line)
