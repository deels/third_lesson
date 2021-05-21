number = input('Введите номер: ')
if number.isdigit() and len(number) == 10:
    print('Валидный номер')
else:
    print('Не является валидным номером')
