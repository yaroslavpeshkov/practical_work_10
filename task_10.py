with open('input.txt', encoding='utf-8') as f:
    with open('output.txt', 'w', encoding='utf-8') as f_1:
        current_day, current_month = map(int, f.readline().split('.'))
        match current_month:
            case 1:
                current_date = current_day
            case 2:
                current_date = 31 + current_day
            case 3:
                current_date = 59 + current_day
            case 4:
                current_date = 90 + current_day
            case 5:
                current_date = 120 + current_day
            case 6:
                current_date = 151 + current_day
            case 7:
                current_date = 181 + current_day
            case 8:
                current_date = 212 + current_day
            case 9:
                current_date = 243 + current_day
            case 10:
                current_date = 273 + current_day
            case 11:
                current_date = 304 + current_day
            case 12:
                current_date = 334 + current_day
        luggage_amount = f.readline()
        for line in f:
            luggage_number, luggage_when = line.split()
            luggage_day, luggage_month = map(int, luggage_when.split('.'))
            match luggage_month:
                case 1:
                    luggage_date = luggage_day
                case 2:
                    luggage_date = 31 + luggage_day
                case 3:
                    luggage_date = 59 + luggage_day
                case 4:
                    luggage_date = 90 + luggage_day
                case 5:
                    luggage_date = 120 + luggage_day
                case 6:
                    luggage_date = 151 + luggage_day
                case 7:
                    luggage_date = 181 + luggage_day
                case 8:
                    luggage_date = 212 + luggage_day
                case 9:
                    luggage_date = 243 + luggage_day
                case 10:
                    luggage_date = 273 + luggage_day
                case 11:
                    luggage_date = 304 + luggage_day
                case 12:
                    luggage_date = 334 + luggage_day
            if current_date - luggage_date > 3:
                f_1.write(luggage_number + '\n')
