first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())
hour = 0
efficency = first_employee + second_employee + third_employee
while students > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    students -= efficency
print(f"Time needed: {hour}h.")