activation_key = input()
command = input()
while command != "Generate":
    instruction = command.split(">>>")
    current_command = instruction[0]
    if current_command == "Contains":
        substring = instruction[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif current_command == "Flip":
        case = instruction[1]
        start_index = int(instruction[2])
        end_index = int(instruction[3])
        if case == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() +\
                             activation_key[end_index:]
        elif case == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + \
                             activation_key[end_index:]
        print(activation_key)
    elif current_command == "Slice":
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")
