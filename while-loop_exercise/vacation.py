vacation = float(input())
balance = float(input())

spend_days = 0
days = 0


while spend_days < 5:
    command = input()
    money = float(input())

    days += 1

    if command == "spend":
        balance = balance - money if balance > money else 0
        spend_days += 1

    else:
        balance += money
        spend_days = 0

    if balance >= vacation:
        print(f"You saved the money for {days} days.")
        break

else:
    print(f"You can't save the money.")
    print(days)












