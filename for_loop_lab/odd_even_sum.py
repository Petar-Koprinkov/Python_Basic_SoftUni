number_of_lines = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, number_of_lines + 1):

    current_number = int(input())

    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")


