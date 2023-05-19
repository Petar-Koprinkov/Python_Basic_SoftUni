exam_hour = int(input())
exam_minutes = int(input())
students_hour = int(input())
students_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
students_time_in_minutes = students_hour * 60 + students_minutes

time_diff = exam_time_in_minutes - students_time_in_minutes

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")


hours = 0
minutes = abs(time_diff)

result = ""

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += f" before the start"
elif time_diff < 0:
    result += f" after the start"

print(result)
