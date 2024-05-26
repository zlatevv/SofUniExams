map_string = input()
destinatons = []
points = 0
for part in map_string.split("=") + map_string.split("/"):
    if len(part) >= 3 and part[0].isupper() and part[1:].isalpha():
        destinatons.append(part)
        points += len(part)

print("Destinations: " + ", ".join(destinatons))
print("Travel Points: " + str(points))