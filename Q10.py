unit_numbers = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez_numbers = ('dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
exceptions = ('onze', 'quinze', 'quatorze')

while True:
    num = int(input("Digite um número entre 1 a 99: "))
    if  num < 1 or num > 99:
        break
    ext = []
    num = list(str(num))
    for x in range(len(num)):
        if x == 0:
            if int(num[0]) == 1:
                if int(num[1]) == 1:
                    ext.append(exceptions[0])
                    break
                elif int(num[1]) == 5:
                    ext.append(exceptions[1])
                    break
                elif int(num[1]) == 4:
                    ext.append(exceptions[2])
                    break
                elif int(num[1]) <= 4:
                    if int(num[1]) == 3:
                        ext.append(''.join(list(unit_numbers[int(num[1]) - 1])[0:3]))
                    else:
                        ext.append(''.join(list(unit_numbers[int(num[1]) - 1])[0:2]))
                    ext.append('ze')
                    break
                elif int(num[1]) >=6:
                    if int(num[1]) == 8:
                        ext.append('dez')
                    else:
                        ext.append('deze')
                    ext.append(str(unit_numbers[int(num[1]) - 1]))
                    break
            else:
                if len(num) == 1:
                    ext.append(str(unit_numbers[int(num[0]) - 1]))
                else:
                    ext.append(str(dez_numbers[int(num[0]) - 1]))
        elif int(num[1]) != 0:
            ext.append('e')
            ext.append(str(unit_numbers[int(num[1]) - 1]))
    num = ' '.join(ext)
    print(num)