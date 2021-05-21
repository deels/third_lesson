name = 'oleg'
name1 = input('Введите имя: ')
if name == name1:
    print(True)
elif name1.lower() == name:
    print(True)
else:
    print('Вы не Олег')
