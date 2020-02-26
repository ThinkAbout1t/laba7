'''Дана послідовність цілих чисел а1, ... a30. Нехай М - найбільше з цих чисел, а m -
найменше. Вивести на екран у порядку зростання всі цілі з інтервалу (m, M), які не
входять до послідовність а1, ... а30.
Виконав Пахомов 122-а
'''
from random import randint
a=[randint(1,20) for i in range(1,5)]
print(a)
m,M=min(a),max(a)
for i in range(m,M+1):
    if i in a:
        continue
    else:
        print(i)
