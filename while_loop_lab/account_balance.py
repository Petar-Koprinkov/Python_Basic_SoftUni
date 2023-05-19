account_balance_sum = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break
    command = float(command)

    if command >= 0:
        account_balance_sum += command
        print(f"Increase: {command:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {account_balance_sum:.2f}")



