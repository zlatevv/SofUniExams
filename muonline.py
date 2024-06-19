health = 100
bitcoin = 0
made_it = True
rooms = input().split("|")
best_room = 0
last_attack = 0
for room in rooms:
    room = room.split()
    command = room[0]
    number = int(room[1])
    if command == "potion":
        best_room += 1
        if health + number > 100:
            number = 100 - health
            health = 100
            print(f"You healed for {number} hp.")
        else:
            health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        best_room += 1
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        last_attack = number
        best_room += 1
        monster = command
        health -= number
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}")
            print(f"Best room: {best_room}")
            made_it = False
            break
if made_it:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")