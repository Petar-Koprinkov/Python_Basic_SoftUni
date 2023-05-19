from sys import maxsize

number = int(input())
max_number = - maxsize
sum_number = 0

for i in range(number):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    sum_number += current_number

sum_number_without_max = sum_number - max_number

if max_number == sum_number_without_max:
    print("Yes" )
    print(f"Sum = {sum_number_without_max}")
else:
    print("No")
    print(f"Diff = {abs(max_number - sum_number_without_max)}")

