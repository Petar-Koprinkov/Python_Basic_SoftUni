from sys import maxsize

max_number = - maxsize
min_number = maxsize

number_of_lines = int(input())

for i in range(number_of_lines):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")


