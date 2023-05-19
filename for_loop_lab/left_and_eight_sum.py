number_of_lines = int(input())

sum_right_numbers = 0
sum_left_numbers = 0

for i in range(number_of_lines):
    right_numbers = int(input())
    sum_right_numbers += right_numbers

for i in range(number_of_lines):
    left_numbers = int(input())
    sum_left_numbers += left_numbers

if sum_right_numbers == sum_left_numbers:
    print(f"Yes, sum = {sum_left_numbers}")
else:
    print(f"No, diff = {abs(sum_right_numbers - sum_left_numbers)}")
