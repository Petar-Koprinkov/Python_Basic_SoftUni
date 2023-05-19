step_walked = 0

while step_walked < 10_000:
    steps = input()

    if steps == "Going home":
        step_walked += int(input())
        break

    step_walked += int(steps)

if step_walked >= 10_000:
    print("Goal reached! Good job!")
    print(f"{step_walked - 10_000} steps over the goal!")
else:
    print(f"{10_000 - step_walked} more steps to reach goal.")

