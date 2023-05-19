flowers_type = input()
flowers_count = int(input())
budged = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

total_price = 0

if flowers_type == "Roses":
    total_price = flowers_count * ROSES_PRICE

    if flowers_count > 80:
        total_price *= 0.90
elif flowers_type == "Dahlias":
    total_price = flowers_count * DAHLIAS_PRICE

    if flowers_count > 90:
        total_price *= 0.85
elif flowers_type == "Tulips":
    total_price = flowers_count * TULIPS_PRICE

    if flowers_count > 80:
        total_price *= 0.85

elif flowers_type == "Narcissus":
    total_price = flowers_count * NARCISSUS_PRICE

    if flowers_count < 120:
        total_price *= 1.15

elif flowers_type == "Gladiolus":
    total_price = flowers_count * GLADIOLUS_PRICE

    if flowers_count < 80:
        total_price *= 1.20

if budged >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budged - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budged:.2f} leva more.")

