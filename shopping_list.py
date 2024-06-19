groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    commands = command.split()
    current_command = commands[0]
    item = commands[1]
    if current_command == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif current_command == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif current_command == "Correct":
        old_item = item
        new_item = commands[2]
        if old_item in groceries:
            old_item_index = groceries.index(old_item)
            groceries[old_item_index] = new_item
    elif current_command == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input()
print(', '.join(map(str, groceries)))