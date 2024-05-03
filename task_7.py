with open('input.txt', 'r', encoding='utf-8') as f:
    lines = []
    for line in f:
        if int(line) != 100:
            lines.append(line)
with open('input.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
