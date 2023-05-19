deposit_price = float(input())
timeline_for_deposit = int(input())
annual_interest_rate = float(input()) / 100

total_sum = deposit_price + timeline_for_deposit * ((deposit_price * annual_interest_rate) / 12)

print(total_sum)

