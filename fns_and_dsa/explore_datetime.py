from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)
    return current_date

def calculate_future_date(now):
    calculate_date = int(input("enter how many day you want to add: "))
    future_date = now + datetime.timedelta(days=calculate_date)
    print(future_date)

now = display_current_datetime()
calculate_future_date(now)