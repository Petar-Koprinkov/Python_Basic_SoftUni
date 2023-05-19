student_name = input()
failed_school_years = 0
total_school_years = 0
total_grade = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        failed_school_years += 1

        if failed_school_years == 2:
            print(f"{student_name} has been excluded at {total_school_years + 1} grade")
            break

    else:
        total_school_years += 1
        total_grade += current_grade
    if total_school_years == 12:
        average_grade = total_grade / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break


