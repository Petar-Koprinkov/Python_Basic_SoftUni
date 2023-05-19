floor_number = int(input())
apartment_number = int(input())

flat_name = None

for floor in range(floor_number, 0, -1):
    for apartment in range(apartment_number):
        if floor == floor_number:
            flat_name = f"L{floor}{apartment}"
        elif floor % 2 == 0:
            flat_name = f"O{floor}{apartment}"
        elif floor % 2 != 0:
            flat_name = f"A{floor}{apartment}"

        print(flat_name, end=" ")
    print()



