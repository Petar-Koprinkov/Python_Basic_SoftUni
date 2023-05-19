chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

PRICE_FOR_CHICKEN_MENU = 10.35
PRICE_FOR_FISH_MENU = 12.40
PRICE_FOR_VEGETARIAN_MENU = 8.15
DELIVERY = 2.50

price_for_food = (chicken_menu * PRICE_FOR_CHICKEN_MENU) + \
                 (fish_menu * PRICE_FOR_FISH_MENU) + \
                 (vegetarian_menu * PRICE_FOR_VEGETARIAN_MENU)

dessert = price_for_food * 0.20

total_price = price_for_food + dessert + DELIVERY

print(total_price)



