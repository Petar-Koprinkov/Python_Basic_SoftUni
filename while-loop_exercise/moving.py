volume = int(input()) * int(input()) * int(input())


while volume > 0:

    command = input()

    if command == "Done":
        print(f"{volume} Cubic meters left.")
        break

    volume -= int(command)

else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
