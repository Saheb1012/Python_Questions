
numbers = [3, 5, 7, 2, 8, 6]

largest = numbers[0]


for number in numbers:
    if number > largest:
        largest = number

print("The largest number in the list is:", largest)
