def days_in_feb(user_year):
    # Check if 'user_year' is a leap year:
    # A leap year is divisible by 4, but not divisible by 100 unless it is divisible by 400.
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        # If it's a leap year, return 29 days for February.
        return 29
    else:
        # If it's not a leap year, return the default 28 days for February.
        return 28
# Prompt the user to enter a year and store the input as an integer in 'user_year'.
user_year = int(input("Enter a year: "))
# Call the 'days_in_feb' function with the user-provided 'user_year' and store the result in 'result'.
result = days_in_feb(user_year)
# Print the result, indicating the number of days in February for the entered year.
print(f"{user_year} has {result} days in February.")
