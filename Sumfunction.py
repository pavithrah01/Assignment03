def sum_list():
    lst = []
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)
    total = 0
    for numb in lst:
        total += int(numb)
    return total


total = sum_list()
print(total)
