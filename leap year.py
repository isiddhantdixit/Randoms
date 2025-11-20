def is_leap(year):
    """
    Check if a given year is a leap year.

    A leap year is divisible by 4, but not by 100 unless also divisible by 400.
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Get user input
year = int(input("Enter year: "))

# Check and display result
if is_leap(year):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))

