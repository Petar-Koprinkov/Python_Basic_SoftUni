total_pieces = int(input()) * int(input())
eaten_pieces = 0

while total_pieces >= eaten_pieces:

    pieces = input()

    if pieces == "STOP":
        print(f"{total_pieces - eaten_pieces} pieces are left.")
        break

    pieces = int(pieces)
    eaten_pieces += pieces

else:
    print(f"No more cake left! You need {eaten_pieces - total_pieces} pieces more.")


