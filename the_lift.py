people = int(input())
the_lift = list(map(int, input().split()))
total_space = len(the_lift) * 4
for wagon in range(len(the_lift)):
    if the_lift[wagon] < 4:
        free = 4 - int(the_lift[wagon])
        if people < free:
            the_lift[wagon] += people
            people = 0
        else:
            the_lift[wagon] += free
            people -= free
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(map(str, the_lift)))
elif sum(the_lift) < total_space:
    print(f"The lift has empty spots!")
    print(' '.join(map(str, the_lift)))
else:
    print(' '.join(map(str, the_lift)))