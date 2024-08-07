numbers = [10, 15, 8, 23, 42, 9, 5, 12]

evens = []
odds = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

print("Even numbers:", evens)
print("Odd numbers:", odds)
