number = int(input())

if number <= 100:
    bonus = 5
elif 100 < number <= 1000:
    bonus = number * 0.20
else:
    bonus = number * 0.10

if number % 2 == 0:
    bonus += 1
elif number % 5 ==0:
    bonus += 2

print(bonus)
print(number + bonus)

