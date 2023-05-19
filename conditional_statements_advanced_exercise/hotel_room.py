month = input()
overnight_stay_count = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if overnight_stay_count > 14:
    price_apartment *= 0.90

if 7 < overnight_stay_count <= 14 and (month == "May" or month == "October"):
    price_studio *= 0.95
elif overnight_stay_count > 14 and (month == "June" or month == "September"):
    price_studio *= 0.80
elif overnight_stay_count > 14 and (month == "May" or month == "October"):
    price_studio *= 0.70

print(f"Apartment: {price_apartment * overnight_stay_count:.2f} lv.")
print(f"Studio: {price_studio * overnight_stay_count:.2f} lv.")

