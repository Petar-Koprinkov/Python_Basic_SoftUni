max_unpleasing_grades = int(input())

unpleasing_grades = 0
total_grade = 0
sum_grade_count = 0
last_task = None

while unpleasing_grades < max_unpleasing_grades:

    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {sum_grade_count}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())

    if grade <= 4:

        unpleasing_grades += 1

    total_grade += grade
    sum_grade_count += 1
    last_task = task_name
    average_grade = total_grade / sum_grade_count

else:
    print(f"You need a break, {max_unpleasing_grades} poor grades.")








