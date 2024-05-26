username = input()
command = input().split()
result = ""
while "Registration" not in command:
    if "Letters" in command:
        if "Lower" in command:
            username = username.lower()
            print(username)
        elif "Upper" in command:
            username = username.upper()
            print(username)
    elif "Reverse" in command:
        try:
            command = list(command)
            start_index = int(command[1])
            end_index = int(command[2])
            result += username[start_index:end_index + 1][::-1]
            print(result)
        except IndexError:
            pass
    elif "Substring" in command:
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif "Replace" in command:
        command = list(command)
        to_replace = command[1]
        if to_replace in username:
            username = username.replace(to_replace, "-")
            print(username)
    elif "IsValid" in command:
        command = list(command)
        char = command[1]
        if char in username:
            print(f"Valid username.")
        else:
            print(f"{char} must be contained in your username.")
    command = input().split()