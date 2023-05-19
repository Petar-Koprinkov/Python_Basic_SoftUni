world_record = float(input())
metres = float(input())
time = float(input())

water_resistence = (metres // 15) * 12.5

swimmer_record = metres * time + water_resistence

if swimmer_record < world_record:
    print(f"Yes, he succeeded! The new world record is {swimmer_record:.2f} seconds.")
elif swimmer_record >= world_record:
    print(f"No, he failed! He was {swimmer_record - world_record:.2f} seconds slower.")



