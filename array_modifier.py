numbers = list(map(int, input().split()))
command = input()
while command != "end":
    command = command.split()
    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        numbers[index1] *= numbers[index2]
    elif command[0] == "decrease":
        for number in range(len(numbers)):
            numbers[number] -= 1
    command = input()
print(', '.join(map(str, numbers)))