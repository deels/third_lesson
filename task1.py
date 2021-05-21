string = input('Введите строку: ')
length = len(string)
if length > 2:
    print(string[0:2] + string[-2] + string[-1])
elif length == 2:
    print(string * 2)
else:
    print("")
