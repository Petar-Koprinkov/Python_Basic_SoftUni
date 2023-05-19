from math import ceil

series = str(input())
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax_time = break_length / 4

needed_time = episode_length + lunch_time + relax_time

if break_length >= needed_time:
    print(f"You have enough time to watch {series} and left with {ceil(break_length - needed_time)} minutes free time")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(needed_time - break_length)} more minutes.")