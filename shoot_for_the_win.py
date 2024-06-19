targets = list(map(int, input().split()))
command = input()

while command != "End":
    index = int(command)
    if index >= 0 and index < len(targets):
        current_target = targets[index]
        for target in range(len(targets)):
            if target == index:
                if targets[index] != -1:
                    targets[index] = -1

                else:
                    continue
            if target != index:
                if targets[target] != -1:
                
                    if targets[target] > current_target:
                        targets[target] -= current_target
                    else:
                        targets[target] += current_target
                else:
                    continue
    command = input()
shot = targets.count(-1)
print(f"Shot targets: {shot} -> {' '.join(map(str, targets))}")