day_stays = int(input())
room_type = input()
rating = input()

price = 0

if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    price = 25
elif room_type == "president apartment":
    price = 35

day_stays -= 1

total_price = price * day_stays

if room_type == "apartment":
    if day_stays < 10:
        total_price *= 0.70
    elif 10 <= day_stays <= 15:
        total_price *= 0.65
    elif day_stays > 15:
        total_price *= 0.50

elif room_type == "president apartment":
    if day_stays < 10:
        total_price *= 0.90
    elif 10 <= day_stays <= 15:
        total_price *= 0.85
    elif day_stays > 15:
        total_price *= 0.80

if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")




