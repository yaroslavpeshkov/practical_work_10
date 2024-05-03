with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        output = ''
        for line in f:
            starting_letter = line[:1]
            output += starting_letter
        f_1.write(output)
