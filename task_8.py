with open('input.txt', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        january_number = 0
        february_number = 0
        march_number = 0
        april_number = 0
        may_number = 0
        june_number = 0
        july_number = 0
        august_number = 0
        september_number = 0
        october_number = 0
        november_number = 0
        december_number = 0
        results = []
        for _ in range(31):
            january_number += int(f.readline())
        january_result = january_number / 31
        f_1.write(str(january_result) + '\n')
        if count == 365:
            for _ in range(28):
                february_number += int(f.readline())
            february_result = february_number / 28
            f_1.write(str(february_result) + '\n')
        else:
            for _ in range(29):
                february_number += int(f.readline())
            february_result = february_number / 29
            f_1.write(str(february_result) + '\n')
        for _ in range(31):
            march_number += int(f.readline())
        march_result = march_number / 31
        f_1.write(str(march_result) + '\n')
        for _ in range(30):
            april_number += int(f.readline())
        april_result = april_number / 30
        f_1.write(str(april_result) + '\n')
        for _ in range(31):
            may_number += int(f.readline())
        may_result = may_number / 31
        f_1.write(str(may_result) + '\n')
        for _ in range(30):
            june_number += int(f.readline())
        june_result = june_number / 30
        f_1.write(str(june_result) + '\n')
        for _ in range(31):
            july_number += int(f.readline())
        july_result = july_number / 31
        f_1.write(str(july_result) + '\n')
        for _ in range(31):
            august_number += int(f.readline())
        august_result = august_number / 31
        f_1.write(str(august_result) + '\n')
        for _ in range(30):
            september_number += int(f.readline())
        september_result = september_number / 30
        f_1.write(str(september_result) + '\n')
        for _ in range(31):
            october_number += int(f.readline())
        october_result = october_number / 31
        f_1.write(str(october_result) + '\n')
        for _ in range(30):
            november_number += int(f.readline())
        november_result = november_number / 30
        f_1.write(str(november_result) + '\n')
        for _ in range(31):
            december_number += int(f.readline())
        december_result = december_number / 31
        f_1.write(str(december_result) + '\n')

