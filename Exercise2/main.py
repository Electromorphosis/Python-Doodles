#Exercise 2
##Part 1: Bubble sort

def BubbleSort(x):
    n = len(x)
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]

'''
x=[1,23,34434,-232,23566,2323423,1,1,0,0,3447,66,77]
BubbleSort(x)

print("Wynik:")
for i in range(len(x)):
    print("%d" % x[i]), 
'''
##Part 2.2 - Permutacje

def silnia_iteracyjna(n):
#    n = input("Enter a number: ")
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            factorial = factorial * i
#    print("Factorail of ", n, " is : ", factorial)
    return factorial

from itertools import permutations

def permutacje(n):
   n=float(n)
   if n < 0:
       print("Błąd. Liczba jest ujemna.")
       return
   if n >= 0 and n < 1:
       print("Błąd. Liczba jest mniejsza od jeden.")
       return
   if n == 1:
       return 1
   if n > 1 and n != int(n):
       print("Błąd. Liczba nie jest całkowita!")
       return
   #cyfr7
   lista_cyfr = str()
   ncp = int(n)
   while (ncp > 0):
       lista_cyfr += (str(ncp))
       ncp -=1
   # lista_cyfr = str(lista_cyfr)
   print('Użyte cyfry: '+str(lista_cyfr))
   #Suma testowa
   suma_testowa = 0
   while (n>1):
        suma_testowa += silnia_iteracyjna(n)
        n-=1

   wszystkie_permutacje = []
   licznik = len(lista_cyfr)
   while (licznik > 0):
       p = permutations(lista_cyfr, licznik)
       # Print the obtained permutations
       for j in list(p):
           print(j)
       # permutacje licz n-1 i dalej
       licznik -= 1


   print("Permutacji w zbiorze jest: "+str(suma_testowa))
   '''#Produkcja permutacji
   lista_permutacji = []
   ncp = n
   x = 1

   licznik = []
   while (x <= ncp):
       licznik.append(x)
       x += 1

   ncp = n
    '''


#n = input("Podaj liczbę do permutacji:")
#permutacje(n)

#2.3
import string
lista_znakow = string.printable
print(lista_znakow)
dlugosc = int(input("Podaj długość hasła:"))
wynik = permutations(lista_znakow, dlugosc)
for j in list(wynik):
    print(j)