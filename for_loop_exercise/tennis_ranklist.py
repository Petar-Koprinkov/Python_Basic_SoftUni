from math import floor

tournaments = int(input())
starting_points = int(input())
gain_points = 0
won_tournaments = 0

for i in range(tournaments):
    result = input()

    if result == "W":
        gain_points += 2000
        won_tournaments += 1
    elif result == "F":
        gain_points += 1200
    elif result == "SF":
        gain_points += 720

print(f"Final points: {starting_points + gain_points}")
print(f"Average points: {floor(gain_points / tournaments)}")
print(f"{won_tournaments / tournaments * 100:.2f}%")










