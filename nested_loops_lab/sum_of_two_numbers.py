first_n = int(input())
second_n = int(input())
magic_n = int(input())

counter = 0
flag = False

for num1 in range(first_n, second_n + 1):
    for num2 in range(first_n, second_n + 1):
        counter += 1
        if num1 + num2 == magic_n:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_n})")
            flag = True
            break

    if flag:
        break
else:
    print(f"{counter} combinations - neither equals {magic_n}")






