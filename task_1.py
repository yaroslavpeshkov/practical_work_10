with open('input.txt', encoding='utf-8') as f:
    output = f.read().upper()
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(output)
