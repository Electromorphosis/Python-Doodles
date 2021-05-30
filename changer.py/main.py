# Open file

f = open("data.txt", "r+")

texts = [
    "Intensywnie koncentruję się na jednej rzeczy",
    "Wymaga ode mnie skupienia się na kilku rzeczach",
    "Nie skupiam się podczas niej na niczym konkretnym",
    "Podczas medytacji utrzymuje przez cały czas jedną, nieruchomą pozycję",
    "Gdy medytuję, wykonuję pewne z góry określone ruchy",
    "W trakcie medytacji pozwalam sobie na wykonywanie dowolnych ruchów",
    "Podczas medytacji skupiam się na doznaniach płynących ze zmysłów",
    "Wykorzystuje wizualizację",
    "Medytując wypowiadam mantrę lub w inny sposób używam głosu",
    "Wywołuję określone postawy lub uczucia w stosunku do samego siebie, innych lub Boga",
    "Przywołuje ważne dla mnie postaci (np. nauczyciela, świętych czy bóstwo) lub wydarzenia z ich życia",
    "Podczas medytacji kontroluję swój oddech",
    "Podczas medytacji używam instrumentu muzycznego"
]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
i = 0

print(str(texts[1]))
print(numbers)


while i < 13:
    numbers.append(i + 1)
    i += 1

with open("data.txt", 'r') as file:
    i = 0
    while i < 13:
        data = file.read().replace(str(texts[i]), str(i))
        i +=1

with open("data.csv", 'w') as file:
    file.write(data)
