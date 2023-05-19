nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
BAGS = 0.40

paint = paint + (paint * 0.10)
nylon = nylon + 2

materials_price = (nylon * NYLON_PRICE) + \
                  (paint * PAINT_PRICE) + \
                  (thinner * THINNER_PRICE) + \
                  BAGS

price_for_working = materials_price * 0.30

total_price = materials_price + (price_for_working * working_hours)

print(total_price)