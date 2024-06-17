without_taxes = 0
total_taxes = 0
with_taxes = 0
is_special = False
is_regular = False
while True:
    text = input()
    if text == "special":
        is_special = True
        break
    elif text == "regular":
        is_regular = True
        break
    parts = float(text)
    if parts < 0:
        print("Invalid price!")
        continue
    without_taxes += parts
    taxes = parts * 0.20
    total_taxes += parts * 0.20
    with_taxes += parts + taxes
    
if with_taxes == 0:
    print("Invalid order!")
else:
    if is_special:
        with_taxes -= with_taxes * 0.10
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {without_taxes:.2f}$\nTaxes: {total_taxes:.2f}$\n-----------\nTotal price: {with_taxes:.2f}$")
