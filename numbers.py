numbers = list(map(int, input().split()))
while True:
    text = input()
    if text == "Finish":
        break
    commands = text.split()
    command = commands[0]
    if command == "Add":
        value = int(commands[1])
        numbers.append(value)
    elif command == "Remove":
        value = int(commands[1])
        if value in numbers:
            numbers.remove(value)
    elif command == "Replace":
        value = int(commands[1])
        replacement = int(commands[2])
        if value in numbers:
            value_place = numbers.index(value)
            numbers[value_place] = replacement
    elif command == "Collapse":
        value = int(commands[1])
        numbers = [number for number in numbers if number >= value]
print(' '.join(map(str, numbers)))