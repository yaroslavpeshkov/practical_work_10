import os

os.mkdir('/Users/simple')
with open('input.txt', encoding='utf-8') as f:
    with open('/Users/simple/output.txt', 'w', encoding='utf-8') as f_1:
        count = 0
        for line in f:
            count += 1
            if count % 2 == 0:
                f_1.write(line)
