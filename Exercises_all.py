import random


# Exercise 1
def code_gen():
    # Starting Input
    code_1 = '79-900'
    code_2 = '80-155'

    # Interpretation
    code1_first_part = ''
    code1_second_part = ''
    for n in code_1:
        if n.isdigit():
            if len(code1_first_part) <= 1:
                code1_first_part += n
            elif len(code1_second_part) <= 2:
                code1_second_part += n
            else:
                break

    x1 = int(code1_first_part)
    x2 = int(code1_second_part)

    code2_first_part = ''
    code2_second_part = ''
    for n in code_2:
        if n.isdigit():
            if len(code2_first_part) <= 1:
                code2_first_part += n
            elif len(code2_second_part) <= 2:
                code2_second_part += n
            else:
                break
    y1 = int(code2_first_part)
    y2 = int(code2_second_part)

    print("Code 1:", str(x1), '-', str(x2), " Code 2:", str(y1), "-", str(y2))

    # List Generator
    code_list = []

    while x1 <= y1:
        if x2 < 999:
            x2 += 1
            code_list.append(str(x1) + '-' + str(x2))
        else:
            x1 += 1
            break

    x2 = 0
    while True:
        if x2 < 149:
            x2 += 1
            code_list.append(str(x1) + '-' + format(x2, '03d'))
        else:
            break

    # Test
    print(code_list)


# Exercise 2
def list_check(n):
    n = int(n)

    # Create full list of values
    test_values = []
    i = 1
    while i <= n:
        test_values.append(i)
        i += 1

    print("All values:", test_values)

    # Checklist creator - random numbers from 1 to n set on the 1/3rd of volume

    checklist = []
    i = 1

    while i < (1 / 3) * n:
        checklist.append(random.randint(1, n))
        i += 1

    print("Input values:", checklist)

    # Output creator
    output_values = test_values

    for x in checklist:
        for y in output_values:
            if x == y:
                output_values.remove(x)

    print('Output:', output_values)


# Exercise 3
def jump():
    j = []
    x = 2
    while x <= 5.5:
        j.append(x)
        x += 0.5

    print(j)
