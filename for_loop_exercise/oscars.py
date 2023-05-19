actor_name = input()
points = float(input())
n = int(input())

MAX_POINTS = 1250.5

for i in range(n):
    judge_name = input()
    points_from_judge = float(input())

    points += len(judge_name) * points_from_judge / 2

    if points > MAX_POINTS:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {MAX_POINTS - points:.1f} more!")



