from time import sleep


a = input('Введите оценки из журнала в формате - \"3/3; 3/3; Н; Н; 7.8/10\"\n').split('; ')
rates = 0
maxRates = 0
for i in a:
    if i != 'Н':
        mark = list(map(float, i.split('/')))
        rates += mark[0]
        maxRates += mark[1]

print('\nRating:', rates / maxRates * 10)

for i in range(20, -1, -1):
    print('\rВыход через:', i, end='')
    sleep(1)