budget = float(input())
extras = int(input())
price_for_clothes = float(input())

decor = budget * 0.10
if extras > 150:
    price_for_clothes *= 0.90

total_price = decor + (extras * price_for_clothes)

if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!" )
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")

