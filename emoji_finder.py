import re
cool_threshold = 1
cool_emojis = []
text = input()
pattern = r"::[A-Z][a-z]{2,}+::|\*\*[A-Z][a-z]{2,}+\*\*"
for_numbers = r"\d"
matches = re.findall(pattern, text)
numbers = re.findall(for_numbers, text)
valid = [match[0] if match[0] else match[1] for match in matches]
for number in numbers:
    cool_threshold *= int(number)
for emoji in matches:
    emoji_coolness = 0
    for character in emoji:
        if character.isalpha():
            emoji_coolness += ord(character)
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid)} emojis found in the text.")
print(f"The cool ones are:")
for i in cool_emojis:
    print(i)