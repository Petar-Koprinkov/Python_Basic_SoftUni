judges = int(input())  # броя съдии
total_grades = 0  # броя оценки
total_grades_sum = 0  # сумата от всички оценки

while True:
    presentation = input()

    if presentation == "Finish":
        break

    grades_sum = 0  # общия брой оценки за едната презентация

    for i in range(judges):
        grades = float(input())  # оценка от съдия
        grades_sum += grades
    total_grades += judges
    total_grades_sum += grades_sum

    print(f"{presentation} - {grades_sum / judges:.2f}.")
print(f"Student's final assessment is {total_grades_sum / total_grades:.2f}.")