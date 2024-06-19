import math
students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
for _ in range(students):
    attendances = int(input())
    current_bonus = (attendances / lectures) * (5 + bonus)
    current_bonus = math.ceil(current_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_student_lectures = attendances
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_student_lectures} lectures.")
