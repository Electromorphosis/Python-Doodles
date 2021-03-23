# Cw. 1
from fileinput import filename

import numpy as np

#Part I
'''
def minimax(list):
    minimum = np.inf
    maksimum = -minimum
    for x in(list):
        if x < minimum:
            minimum = x
        if x > maksimum:
            maksimum = x
    print("maksimum:", maksimum, "minimum:", minimum)


lista = [-233, 8, 23, 573, 2323 ]
'''
#minimax(lista)

#Part II
'''
def rek_silnia(n):
    print("Wybrałeś:", n)
    if n < 1 or n % 1 != 0: #Ending procedure
        if n == 0:
           return 0
        else:
            return
    if n == 1:
        return 1
    wynik = n * rek_silnia(n-1)
    return wynik


while True:
    try:
        y=int(input('Podaj liczbe do silni:'))
    except:
        print("Input error")
        continue
    print('Silnia wynosi:', rek_silnia(y))
    loop_switch=input('Powtórzyć(T/N)?')
    if loop_switch == 'N':
        break
'''
#Part III
#Działa dla plików w dostępie administratora?
def podmiana():

    x=input('Podaj słowo, które chcesz podmienić:')
    y=input('Podaj słowo, na jakie chcesz podmienić:')
    nazwa=input('Podaj adres pliku do podmianki:')
    with open(nazwa, 'r') as file:
        data = file.read().replace(x, y)
    with open(nazwa, 'w') as file:
        file.write(data)


#Part IV
def licznik():
    nazwa = input('Podaj adres pliku do podsumowania:')
    plik = str(open(nazwa, 'r'))
    all_freq = {}
    suma = 0
    for i in plik:
        if i in all_freq:
            all_freq[i] += 1
            suma += 1
        else:
            all_freq[i] = 1
    print("Count of all characters:\n "
          + str(all_freq))
    print("Suma znaków: " + str(suma))
    all_percent = {}
    for i in all_freq:
        all_percent[i] = all_freq[i] / suma
    for i in all_percent:
        print('\n'+str(i)+':', end=' ')
        all_percent[i] = int(all_percent[i]*100)
        print(str(all_percent[i])+'%')
        while all_percent[i] > 0:
            print('-', end=' ')
            all_percent[i] -= 1


licznik()