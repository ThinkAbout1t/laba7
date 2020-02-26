'''Задача. Визначити комп'ютер, виготовлений фірмою AMD з мінімальною ціною і
вивести всі відомості про нього. Поля структури: Виробник, Обсяг оперативної пам’яті,
Дата виготовлення, Ціна.
Виконав Пахомов 122-а
'''
min_val=[]
comp = ['comp1','comp2','comp3','comp4','comp5']
company = ['AMD', 'AMD', 'GTX', 'Lenovo', 'Samsung']
cost = [2300, 2600, 4444, 228322, 1234]
operativka = [1000, 1233, 13132, 1231, 1133]
data = ['27.02.2020', '28.06.2018', '12.02.2017', '02.02.2020', '14.12.2021']
d_company = {b: n for (b, n) in zip(comp, company)}
d_cost = {a: s for (a, s) in zip(comp, cost)}
d_operativka={z: x for (z, x) in zip(comp, operativka)}
d_data={q: w for (q, w) in zip(comp, data)}
for i in d_company.keys():
    if d_company[i] == 'AMD':
        min_val.append(d_cost[i])
a=min(min_val)
for i in d_cost.keys():
    if d_cost[i] == a:
        print(f'AMD: Cots:{d_cost[i]}, Operativka:{d_operativka[i]}, Data:{d_data[i]}')
