
numbers = [5, 4, 9, 2, 3, 8]

sum_even = 0
sum_odd = 0
for number in numbers:
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
result = (sum_even, sum_odd)

print(result)
