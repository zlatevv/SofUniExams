current_command = input()
cities = {}
while current_command != "Sail":
    information = current_command.split("||")
    city = information[0]
    population = int(information[1])
    gold = int(information[2])
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold
    current_command = input()
text = input()
while text != "End":
    commands = text.split("=>")
    command = commands[0]
    town = commands[1]
    if command == "Plunder":
        people = int(commands[2])
        gold = int(commands[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif command == 'Prosper':
        gold = int(commands[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    text = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in cities.items():
        population, gold = info
        print(f"{city} -> Population: {population} citizens, Gold: {gold} kg ")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
