chest = input().split("|")
text = input()
while text != "Yohoho!":
    commands = text.split()
    command = commands[0]
    if command == "Loot":
        items = commands[1:]
        for item in items:
            if item not in chest:
                chest.insert(0, item)
    elif command == "Drop":
        index = int(commands[1])
        if index >= 0 and index < len(chest):
            item_to_remove = chest[index]
            chest.remove(item_to_remove)
            chest.append(item_to_remove)
    elif command == "Steal":
        count = int(commands[1])
        if count < len(chest):
            stolen = chest[-count:]
            chest = chest[:-count]
        else:
            count = len(chest)
            stolen = chest[-count:]
            chest = chest[:-count]
        print(', '.join(map(str, stolen)))
    text = input()
if chest:
    total = 0
    for loot in chest:
        total += len(loot)
    average = total / len(chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")