prime_number = 0
non_prime_number = 0


while True:

    command = input()

    if command == "stop":
        break

    current_number = int(command)
    flag = False

    if current_number < 0:
        print("Number is negative.")
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            flag = True
            break

    if flag:
        non_prime_number += current_number
    else:
        prime_number += current_number

print(f"Sum of all prime numbers is: {prime_number}")
print(f"Sum of all non prime number is: {non_prime_number}")


