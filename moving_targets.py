targets = list(map(int, input().split()))
commands = input()
while commands != "End":
    commands = commands.split()
    command = commands[0]
    index = int(commands[1])
    if command == "Shoot":
        power = int(commands[2])
        if index >= 0 and index < len(targets):
            if targets[index] > 0:
                targets[index] -= power
                if targets[index] <= 0:
                    targets.pop(index)
    elif command == "Add":
        value = int(commands[2])
        if index >= 0 and index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        radius = int(commands[2])
        if index - radius >= 0 and index + radius < len(targets):
            targets = targets[:index - radius] + targets[index + radius + 1:]
        else:
            print("Strike missed!")
    commands = input()
print('|'.join(map(str, targets)))