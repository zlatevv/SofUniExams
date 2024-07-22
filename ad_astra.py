import re
total = 0
food = []
text = input()
pattern = r"#([a-zA-Z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([a-zA-Z\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|"
matches = re.findall(pattern, text)
for match in matches:
    if match[0]:
        item_name = match[0]
        expiration_date = match[1]
        calories = int(match[2])
    else:
        item_name = match[3]
        expiration_date = match[4]
        calories = int(match[5])

    total += calories
    food.append((item_name, expiration_date, calories))
print(f"You have food to last you for: {total // 2000} days!")
for item in food:
    name = item[0]
    date = item[1]
    nutrition = int(item[2])
    print(f"Item: {name}, Best before: {date}, Nutrition: {nutrition}")
