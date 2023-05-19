from sys import maxsize

min_number = maxsize

while True:

    command = input()

    if command == "Stop":
        break

    command = int(command)

    if command < min_number:
        min_number = command

print(min_number)

