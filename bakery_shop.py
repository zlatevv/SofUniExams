line = input().split()
foods = {}
all_sold = 0
while "Complete" not in line:
    if line[0] == "Receive":
        quantity = int(line[1])
        food = line[2]
        if food not in foods:
            foods[food] = quantity
        elif food in foods:
            foods[food] += quantity
        if quantity <= 0:
            continue
    elif line[0] == "Sell":
        quantity = int(line[1])
        food = line[2]
        if food not in foods:
            print(f"You do not have any {food}.")
        elif quantity > foods[food]:
            print(f"There aren't enough {food}. You sold the last {foods[food]} of them.")
            all_sold += foods[food]
            del foods[food]
        else:
            print(f"You sold {quantity} {food}.")
            foods[food] -= quantity
            all_sold += quantity
            if foods[food] <= 0:
                del foods[food]


    line = input().split()
for food, quantity in foods.items():
    print(f"{food}: {quantity}")
print(f"All sold: {all_sold} goods.")