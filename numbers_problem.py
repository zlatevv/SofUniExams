numbers = list(map(int, input().split()))
average_number = sum(numbers) // len(numbers)
top_numbers = []

for number in numbers:
    if number > average_number:
        top_numbers.append(number)
if top_numbers:
    print(' '.join(map(str, sorted(top_numbers, reverse=True)[:5])))
else:
    print("No")