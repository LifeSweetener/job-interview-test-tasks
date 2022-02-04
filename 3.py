def read_line(j = 0):
    global file  # работа с глобальной переменной file
    str = ""
    while (str.find('\n') == -1):
        str += file.readline()
        if (str == ""):
            break
    
    return str

def print_guard(number):
    global guards  # работа с глобальной переменной guards
    guard = guards.get(str(number))
    for date in guard.keys():
        print(date)
        minutes = guard.get(date)
        for minute in minutes:
            print(" | " + str(minute[0]) + " | " + str(minute[1]) + " | ")

#====================================================
#====================================================

guards = dict()  # Строящаяся таблица со всеми записями об охране
current_guard = -1  # Текущий обрабатываемый охранник (номер)

file = open("C:\\Users\\User_ll\\Downloads\\04.txt")  # Открытие файла с журналом (исходные данные)
line = read_line()  # Начало считывания исходных данных (см. функцию выше)
data = ""  # хранилище данных
while (line != ""):
    data += line
    line = read_line()
file.close()  # здесь закрыть файл

data = data.split('\n')  # сделать список из исходных данных...
data.sort(key = lambda x: x[2:18])  # и сортировать его для более удобной дальнейшей обработки

counter = 0  # счётчик записей
while (counter < len(data)):
    if (line.find('#') != -1):  # если заступает другой охранник...
        start = line.find('#')  # определение номера охранника
        next = start + 1
        number = ""  # номер
        while (line[next].isdigit()):
            number += line[next]
            next += 1
        
        current_guard = number  # пометка номера текущего охранника
        
        counter += 1
        if (counter == len(data)):
            break
        line = data[counter]  # считать записи времени бодрствования и сна охранника...
        while (line != "") and (line.find('#') == -1):  # цикл считывания времени "wakes up" и "falls asleep"
            date = line[6:11]  # дата очередной записи
            time = line[15:17]  # время этой записи
            sleep = True  # просыпается охранник или засыпает?..
            if (line.find("sleep") == -1):
                sleep = False
            
            # обновить главную таблицу guards:
            if (not (current_guard in guards) ):
                guards[current_guard] = dict()
                guards[current_guard][date] = [ [int(time), sleep] ]
            else:
                if (not (date in guards[current_guard]) ):
                    guards[current_guard][date] = [ [int(time), sleep] ]
                else:
                    guards[current_guard].get(date).append([int(time), sleep])
           
           # перейти к следующей записи:
            counter += 1
            if (counter == len(data)):
                break
            line = data[counter]
    else:
        if (current_guard == -1):
            counter += 1
            if (counter == len(data)):
                break
            line = data[counter]
            continue

# этот цикл дописывает недостающие минуты в главную таблицу
for number in guards.keys():
    guard = guards.get(number)
    for date in guard.keys():
        minutes = guard.get(date)
        minutes.sort()  # сортировка по минутам
        minutes2 = []  # обновлённые минуты
        for minute in range(0, len(minutes), 2):
            if (minute == 0):
                for i in range(1, minutes[minute][0]):
                    minutes2.insert(i, [i, False] )
            if (minute == len(minutes) - 1):
                for i in range(minutes[minute][0], 61):
                    minutes2.insert(i, [i, minutes[minute][1]] )
                break
            for i in range(minutes[minute][0], minutes[minute + 1][0]):
                minutes2.insert(i, [i, minutes[minute][1]] )
            if (minute == len(minutes) - 2):
                for i in range(minutes[minute + 1][0], 61):
                    minutes2.insert(i, [i, minutes[minute + 1][1]] )
                break
        guard[date] = minutes2

n_max = -1
minute_max = -1
guard_max = -1
for number in guards.keys():
    times = [0] * 60  # массив из 60-ти минут с кол-вом раз, когда охранник спал в эту минуту
    guard = guards.get(number)
    for date in guard.keys():
        minutes = guard.get(date)
        minutes.sort()  # сортировка по минутам
        for minute in minutes:
            if (minute[1] == True):  # если охранник в текущую минуту спал,..
                times[minute[0]-1] += 1  # то счётчик инкрементируется
        
    for i in range(60):  # определение максимального
        if (times[i] > n_max):
            n_max = times[i]
            minute_max = i + 1
            guard_max = int(number)

print(minute_max*guard_max)