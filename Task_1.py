str_time = '1h 45m,360s,25m,30m 120s,2h 60s'
'''
Задание 1
Строка содержит пять временных значений. Они записаны через запятую:
'1h 45m,360s,25m,30m 120s,2h 60s'.
Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы split(), replace() и оператор in.

Сначала сделал более сложный вариант, потом понял, что это не нужно
list_time = [t.split(' ') for t in str_time.split(',')]
all_minutes = []
for hms in list_time:
    all_t = 0
    for t in hms:
        if t[-1] == 'h':
            all_t += int(t[:-1]) * 60
        elif t[-1] == 's':
            all_t += int(t[:-1]) / 60
        elif t[-1] == 'm':
            all_t += int(t[:-1]) 
        all_minutes.append(all_t)
        print(all_t)
print(sum(all_minutes))
'''
list_time = str_time.replace(',',' ').split()
total_minutes = 0
for t in list(list_time):
    if t[-1] == 'h':
        total_minutes += int(t[:-1]) * 60
    elif t[-1] == 's':
        total_minutes+= int(int(t[:-1]) / 60)
    elif t[-1] == 'm':
        total_minutes += int(t[:-1]) 

print(total_minutes)