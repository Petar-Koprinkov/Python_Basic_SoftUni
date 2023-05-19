age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_from_gifts = 0
money_given = 10
taken_form_brother = 1

for i in range(1, age+1):
    if i % 2 == 0:
        money_from_gifts += money_given - taken_form_brother
        money_given += 10
    else:
        money_from_gifts += toy_price

if money_from_gifts >= washing_machine_price:
    print(f"Yes! {money_from_gifts - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price- money_from_gifts:.2f}")