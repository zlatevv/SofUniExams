from math import ceil
budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_egg = float(input())
price_for_apron = float(input())
total = 0
free_packages = 0
for student in range(1, students + 1):
    if student % 5 == 0:
        free_packages += 1
total += price_for_apron * (students + ceil(students * 0.2)) + price_for_egg * 10 * students + price_for_flour * \
         (students - free_packages)
if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    needed = total - budget
    print(f"{needed:.2f}$ more needed.")
