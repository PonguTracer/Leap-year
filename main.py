def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29
    else:
        return 28

user_year = int(input("Enter a year: "))
result = days_in_feb(user_year)
print(f"{user_year} has {result} days in February.")
