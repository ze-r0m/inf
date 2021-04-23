name = ['Петров Никита','Иванов Иван','Киселев Дмитрий','Охтаров Андрей','Погорелов Антон','Карташов Петр']
a = [[3,4,4,5],[5,5,5,5],[4,4,4,5],[4,4,4,5],[5,4,4,5],[2,3,4,4]]
pr = ['Матем.','Англ.','Фил-я','Инф.']
b = 0

# №1 №2
print()
print('1, 2 Задание')
for i in range(len(name)):
    summ = 0
    for j in range(len(a[i])):
        summ += a[i][j]
        sred = summ/4
    print(name[i],':', a[i],'Средняя оценка: ',sred)

#3
print()
print('3 Задание')
for n in range(len(a[i])):
    sr=0
    for p in range(len(a)):
        sr+=a[p][n]
    print(pr[n],':',round(sr/6,2))

#4
print()
print('4 Задание')
print('Получают повышенную стипендию: ')
for i in range(len(name)):
    k = 0
    for j in range(len(a[i])):
        if a[i][j] == 5:
            k+=1
    if k == 4:
        print(name[i])

#5
print()
print('5 Задание')
print('Получают стипендию:')
for i in range(len(name)):
    k = 0
    for j in range(len(a[i])):
        if (a[i][j] == 5) or (a[i][j] == 4):
            k+=1
    if k == 4:
        b+=1
print(b, 'человек(а)')

#6
print()
print('6 Задание')
print('Не успевают по заданной дисциплине:')
for i in range(len(name)):
    k = 0
    for j in range(len(a[i])):
        if a[i][j] == 2:
            k+=1
    if k >= 1:
        print(name[i])

