# Cw. 1
import numpy as np

#Part I

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

#minimax(lista)

#Part II

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

#Part III

def podmiana(x,y):
    x=input('Podaj słowo, które chcesz podmienić:')
    y=input('Podaj słowo, na jakie chcesz podmienić:')
    