screening_type = input()
r = int(input())
c = int(input())

cinema_capacity = r * c

PREMIERE_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

income = 0

if screening_type == "Premiere":
    income = cinema_capacity * PREMIERE_PRICE
elif screening_type == "Normal":
    income = cinema_capacity * NORMAL_PRICE
elif screening_type == "Discount":
    income = cinema_capacity * DISCOUNT_PRICE

print(f"{income:.2f} leva")
