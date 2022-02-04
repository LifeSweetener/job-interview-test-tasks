# Подготовить исходные данные для обработки:
file = open("C:\\Users\\User_ll\\Downloads\\07.txt")
data = file.readlines()
file.close()

counter = 0
ok = False
for address in data:
    bab = list()
    bab_len = 0  # кол-во пар квадратных скобок (= кол-ву элементов списка "bab")
    
    ## Найти все символы в квадратных скобках и положить в список "bab":
    i = address.find("[")
    while (i < len(address)) and (i != -1):
        bab.append("")
        symb = address[i+1]
        while (symb != ']'):
            bab[bab_len] += symb
            i += 1
            symb = address[i+1]
        
        # перейти к следующей паре квадратных скобок:
        i += 2
        bab_len += 1
        i = address.find("[", i)
    
    its_bab = False
    for i in range(1, len(address) - 1):
        troika_aba = str(address[i-1]) + str(address[i]) + str(address[i+1])
        
        # проверка, что не считываются символы в квадратных скобках:
        if (str(address[i+1]) == '['):
            its_bab = True
        if (str(address[i-1]) == ']'):
            its_bab = False
            continue
        if (its_bab):
            continue
        
        # сравнивание тройки "aba" с тройкой "bab":
        for j in bab:
            if (ok):
                break
            for k in range(1, len(j) - 1):
                troika_bab = str(j[k-1]) + str(j[k]) + str(j[k+1])
                if (troika_aba[0] == troika_bab[1]) and (troika_aba[2] == troika_bab[1]) and (troika_aba[1] == troika_bab[0]) and (troika_aba[1] == troika_bab[2]):
                    counter += 1
                    ok = True
                    break
                    
        if (ok):
            ok = False
            break

print(counter)