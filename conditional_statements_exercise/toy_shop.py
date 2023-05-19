excursion = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())

PUZZLE_PRICE = 2.60
TALKING_BEAR_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINIONS_PRICE = 8.20
TRUCKS_PRICE = 2

total_toy = puzzle + talking_doll + teddy_bear + minions + trucks
total_toy_price = (puzzle * PUZZLE_PRICE) + \
                  (talking_doll * TALKING_BEAR_PRICE) + \
                  (teddy_bear * TEDDY_BEAR_PRICE) + \
                  (minions * MINIONS_PRICE) + \
                  (trucks * TRUCKS_PRICE)
if total_toy >= 50:
    total_toy_price = total_toy_price * 0.75

total_toy_price = total_toy_price * 0.90

if total_toy_price >= excursion:
    print(f"Yes! {total_toy_price - excursion:.2f} lv left.")
else:
    print(f"Not enough money! {excursion - total_toy_price:.2f} lv needed.")

