import re

score = 0
destinations = input()
pattern = r"=([A-Z][A-Za-z]{2,})=|\/([A-Z][A-Za-z]{2,})\/"
matches = re.findall(pattern, destinations)
valid = [match[0] if match[0] else match[1] for match in matches]
for current_destination in valid:
    score += len(current_destination)
print(f"Destinations: {', '.join(valid)}")
print(f"Travel Points: {score}")
