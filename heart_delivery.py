neighborhood = list(map(int, input().split("@")))
command = input()
cupid_location = 0
while command != "Love!":
    jumps = command.split()
    destination = int(jumps[1])
    cupid_location += destination
    if cupid_location >= len(neighborhood):
        cupid_location = 0
    if neighborhood[cupid_location] == 0:
        print(f"Place {cupid_location} already had Valentine's day.")
    elif neighborhood[cupid_location] != 0:
        neighborhood[cupid_location] -= 2
        if neighborhood[cupid_location] == 0:
            print(f"Place {cupid_location} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {cupid_location}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    successful_houses = neighborhood.count(0)
    failed_houses = len(neighborhood) - successful_houses
    print(f"Cupid has failed {failed_houses} places.")