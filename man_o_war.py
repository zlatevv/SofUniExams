ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health = int(input())
text = input()
won = False
lost = False
while text != "Retire":
    commands = text.split()
    command = commands[0]
    if command == "Fire":
        index = int(commands[1])
        damage = int(commands[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                won = True
                break
        if won:
            break
    elif command == "Defend":
        start_index = int(commands[1])
        end_index = int(commands[2])
        damage = int(commands[3])
        if 0 <= start_index < len(ship) and 0 <= end_index < len(ship) and start_index < end_index:
            for section in range(start_index, end_index + 1):
                ship[section] -= damage
                if ship[section] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    lost = True
                    break
        if lost:
            break
    elif command == "Repair":
        index = int(commands[1])
        health = int(commands[2])
        if 0 <= index < len(ship):
            if ship[index] + health < maximum_health:
                ship[index] += health
            else:
                ship[index] = maximum_health
    elif command == "Status":
        need_a_repair = 0
        for section in ship:
            if section < maximum_health * 0.2:
                need_a_repair += 1
        print(f"{need_a_repair} sections need repair.")
    text = input()
if not lost and not won:
    print(f"Pirate ship status: {sum(ship)}")
    print(f"Warship status: {sum(warship)}")