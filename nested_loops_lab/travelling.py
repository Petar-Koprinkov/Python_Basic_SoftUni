while True:

    destination = input()

    if destination == "End":
        break

    balance = 0
    travel_money = float(input())

    while balance < travel_money:

        money = float(input())
        balance += money

    print(f"Going to {destination}!")




