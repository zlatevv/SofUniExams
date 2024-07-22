message = input()
command = input()
while command != "Decode":
    instructions = command.split("|")
    current_command = instructions[0]
    if current_command == "Move":
        number = int(instructions[1])
        message = message[number:] + message[:number]
    elif current_command == "Insert":
        index = int(instructions[1])
        value = instructions[2]
        message = list(message)
        message.insert(index, value)
    elif current_command == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        message = list(message)
        for index in range(len(message)):
            if message[index] == substring:
                message[index] = replacement

    command = input()
print(f"The decrypted message is: {''.join(message)}")

