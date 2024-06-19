inventory = input().split(", ")
text = input()
while text != "Craft!":
    commands = text.split(" - ")
    command = commands[0]
    items = commands[1]
    if command == "Collect":
        if items not in inventory:
            inventory.append(items)
    elif command == "Drop":
        if items in inventory:
            inventory.remove(items)
    elif command == "Combine Items":
        items = items.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)
    elif command == "Renew":
        if items in inventory:
            inventory.remove(items)
            inventory.append(items)
    text = input()
print(', '.join(map(str, inventory)))