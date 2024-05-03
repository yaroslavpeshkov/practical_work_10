with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        for line in f:
            starting_letter = line[:1]
            if starting_letter.lower() == 'a':
                f_1.write(line)
