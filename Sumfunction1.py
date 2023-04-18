def sum_list():
    numbers = input("Enter a list of numbers, separated by commas: ")
    numbers_list = numbers.split(",")
    total = 0
    for num in numbers_list:
        total += int(num)
    return total
total = sum_list()
print(total)
