city = input()
volume_sale = float(input())

commission = 0

correct_statement = True

if city == "Sofia":
    if 0 <= volume_sale <= 500:
        commission = volume_sale * 0.05
    elif 500 < volume_sale <= 1000:
        commission = volume_sale * 0.07
    elif 1000 < volume_sale <= 10000:
        commission = volume_sale * 0.08
    elif volume_sale > 10000:
        commission = volume_sale * 0.12
    else:
        correct_statement = False
elif city == "Varna":
    if 0 <= volume_sale <= 500:
        commission = volume_sale * 0.045
    elif 500 < volume_sale <= 1000:
        commission = volume_sale * 0.075
    elif 1000 < volume_sale <= 10000:
        commission = volume_sale * 0.10
    elif volume_sale > 10000:
        commission = volume_sale * 0.13
    else:
        correct_statement = False
elif city == "Plovdiv":
    if 0 <= volume_sale <= 500:
        commission = volume_sale * 0.055
    elif 500 < volume_sale <= 1000:
        commission = volume_sale * 0.08
    elif 1000 < volume_sale <= 10000:
        commission = volume_sale * 0.12
    elif volume_sale > 10000:
        commission = volume_sale * 0.145
    else:
        correct_statement = False
else:
    correct_statement = False

if correct_statement:
    print(f"{commission:.2f}")
else:
    print("error")

