pen_packs = int(input())
market_packs = int(input())
detergent_packs = int(input())
discount = int(input()) / 100

PEN_PRICE = 5.80
MARKET_PRICE = 7.20
DETERGENT_PRICE = 1.20

price = (pen_packs * PEN_PRICE) + (market_packs * MARKET_PRICE) + (detergent_packs * DETERGENT_PRICE)
discount_price = price * discount
total_price = price - discount_price

print(total_price)
