from sys import maxsize
max_number = - maxsize

while True:
    command = input()
    if command == "Stop":
        break
    command = int(command)

    if command > max_number:
        max_number = command
print(max_number)


