numbers_of_page = int(input())
page_for_one_hour = int(input())
days = int(input())

needed_time_to_read_book = numbers_of_page // page_for_one_hour
needed_hours_to_read_book = needed_time_to_read_book // days

print(needed_hours_to_read_book)