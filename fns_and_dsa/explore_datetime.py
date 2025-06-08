from datetime import datetime, timedelta

FORMAT = "%Y-%m-%d %H:%M:%S"

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(now):
    calculate_date = int(input("Enter the number of days to add to the current date: "))
    future_date = now + timedelta(days=calculate_date)
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))

now = display_current_datetime()
calculate_future_date(now)