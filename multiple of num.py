num = 5
limit = 25

for multiple in range(num, limit + 1, num):
    
    print(multiple, end=', ' if multiple + num <= limit else '')
