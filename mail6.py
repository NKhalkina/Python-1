'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна 
сумме последних трех.Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
программу, которая проверяет счастливость билета.'''

n=int(input('Введите шестизначный номер билета:'))
summa1=0
a=n%10
b=n//10
c=b%10
d=b//10
e=d%10
summa1=a+c+e
summa2=0
a1=d//10
b1=a1%10
c1=a1//10
d1=c1%10
e1=c1//10
summa2=b1+d1+e1
if summa1==summa2:
    print('Ваш билет счастливый!')
else:
    print('Извините, ваш билет не счастливый. Прокатитесь еще раз и вам точно повезет!')



