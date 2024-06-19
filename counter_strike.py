def battle(energy):
    won_battles = 0
    while True:
        command = input()
        if command == "End of battle":
            return f"Won battles: {won_battles}. Energy left: {energy}"
        distance = int(command)
        if energy >= distance:
            energy -= distance
            won_battles += 1
            if won_battles % 3 == 0:
                energy += won_battles
        else:
            return f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy"


energy = int(input())
result = battle(energy)
print(result)

