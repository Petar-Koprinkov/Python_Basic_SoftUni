bottle_of_detergent = int(input())

clean_plate_count = 0
clean_pot_count = 0
total_detergent = 0
counter = 0
total_detergent_sum = 0

while True:
    container = input()
    total_detergent = bottle_of_detergent * 750

    if container == "End":
        print(f"Detergent was enough!")
        print(f"{clean_plate_count} dishes and {clean_pot_count} pots were washed.")
        print(f"Leftover detergent {total_detergent - total_detergent_sum} ml.")
        break

    container = int(container)
    counter += 1

    if counter % 3 == 0:
        clean_pot_count += container
        total_detergent_sum += container * 15

    else:
        clean_plate_count += container
        total_detergent_sum += container * 5

    if total_detergent_sum > total_detergent:
        print(f"Not enough detergent, {abs(total_detergent - total_detergent_sum)} ml. more necessary!")
        break