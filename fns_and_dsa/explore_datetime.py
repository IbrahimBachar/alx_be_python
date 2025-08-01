from datetime import datetime, date
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days = number_of_days)

    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()