text = input()
letter_sum = 0

for i in text:
    if i == "a":
        letter_sum += 1
    if i == "e":
        letter_sum += 2
    if i == "i":
        letter_sum += 3
    if i == "o":
        letter_sum += 4
    if i == "u":
        letter_sum += 5

print(letter_sum)

