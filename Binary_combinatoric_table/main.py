import time

def progressbar(current, total, bar_length=20):
    if current < 0 or total < 0 or current > total:
        print('[Progress bar error - wrong range setting!]')
        exit()

    percent = round(int(current) / int(total) * 100)

    if int(current) != int(total):
        arrow = str('-' * int(percent / 5) + '>')
    elif current == 0:
        arrow = ''
    else:
        arrow = '-' * 20
    spaces = ' ' * (bar_length - len(arrow))

    print('Progress: [' + str(arrow) + str(spaces) + '] ' + str(percent) + '%', end='\r')


def digitizer(x):
    y = 1
    while x > 0:
        y *= 10
        x -= 1

    return y

def listToString(list):
    str1 = " "
    return (str1.join(list))


def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


# Banner & Opening
print("===Binary Combinator===")
while True:
    number = int(input("Enter maximum digit of binary numbers generated:"))
    if number > 0:
        break
    print("Wrong number, try again...")
print("You've chosen " + str(number))
print("===Loading numbers database (not really, just loading bar added for premium aggro lol)===")

print('Loading progress:')
print('\n')
i = 0
#while i <= 20:
#    time.sleep(0.1)
#    progressbar(i, 20)
#    time.sleep(0.1)
#    i += 1
# IDK if progress bar works... need to be tested in a console, not IDE

i = "0"
digits = digitizer(number)
while int(i) < (digits):
    print(i)
    time.sleep(0.01)
    i = i.replace("0", "1", 1)
    if int(i) % 10 == 1:
        print(i)
        j = getSum(i)
        i = i.replace("1", "0", j)
        i = i.replace("0", "1", 1)
        i += '0'
