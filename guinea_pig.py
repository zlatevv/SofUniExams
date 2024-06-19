food = float(input())
hay = float(input())
cover = float(input())
not_enough = False
pig_weight = float(input())
for day in range(1, 31):
    if round(food) <= 0 or round(hay) <= 0 or round(cover) <= 0:
        not_enough = True
        break
    food -= 0.3
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= pig_weight * (1/3)
if not not_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")