import datetime

# Read the input
input_date = input("month day year").strip()

# Split the input into month, day, and year
month, day, year = map(int, input_date.split())

# Create a date object
date_object = datetime.date(year, month, day)

# Get the day of the week in uppercase
day_of_week = date_object.strftime("%A").upper()

# Print the result
print(day_of_week)