'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).'''

n=int(input('Введите число долек n:'))
m=int(input('Введите число долек m:'))
k=int(input('Введите число долек k, которые нужно отломить:'))
if k%n==0 or k%m==0:
    print(f'От шоколадки размером {n} x {m} можно отломить {k} долек одним разломом')
else:
    print(f'От шоколадки размером {n} x {m} нельзя отломить {k} долек одним разломом')
