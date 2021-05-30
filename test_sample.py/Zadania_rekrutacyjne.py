# Exercise 1

# Starting Input
proper_code = False
string = ''

while not proper_code:
    string = input("Enter postal code:")
    if sum(c.isdigit() for c in string) == 5:
        proper_code = True
    else:
        print("Wrong input! Try again.")

# Interpreting Input
raw_code = list(string)
first_part = ''
second_part = ''

for n in raw_code:
    if n.isdigit():
        if len(first_part) <= 1:
            first_part += n
        elif len(second_part) <= 2:
            second_part += n
        else:
            break

print("Your number is: ", str(first_part), "-", str(second_part))

# Starting Input
proper_code = False
string = ''

while not proper_code:
    string = input("Enter postal code:")
    if sum(c.isdigit() for c in string) == 5:
        proper_code = True
    else:
        print("Wrong input! Try again.")

# Interpreting Input
raw_code = list(string)
first_part = ''
second_part = ''

for n in raw_code:
    if n.isdigit():
        if len(first_part) <= 1:
            first_part += n
        elif len(second_part) <= 2:
            second_part += n
        else:
            break

print("Your number is: ", str(first_part), "-", str(second_part))
