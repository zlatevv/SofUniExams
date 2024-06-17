elements = input().split()
moves = 0
while True:
    command = input().split()
    if "end" in command:
        break
    moves += 1
    index1, index2 = map(int, command)
    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(elements) or index2 >= len(elements):
        middle_index = len(elements) // 2
        elements.insert(middle_index, f'-{moves}a')
        elements.insert(middle_index + 1, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board!")
        continue

    if elements[index1] == elements[index2]:
        print(f"Congrats! You found matching elements - {elements[index1]}!")
        new_elements = []
        for key, element in enumerate(elements):
            if key != index1 and key!= index2:
                new_elements.append(element)
        elements = new_elements
    else:
        print("Try again!")
    if not elements:
        print(f"You have won in {moves} turns!")
        break

if elements:
    print(f"Sorry you lose :(")
    print(' '.join(map(str, elements)))