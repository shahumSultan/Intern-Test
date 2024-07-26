# leap_year.py

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
        # The year is also evenly divisible by 400. Then it is a leap year.

def is_leap_year(year):
    # CODE BELOW THIS LINE
    if (year%100==0):
        print("Its Not Leap Year")
    elif((year%4==0) and (year%100!=0)):
        print("Its Leap Year")
    else:
        print("Its Not Leap Year")
    return

if __name__ == "__main__":
    year = int(input("Enter year:\t"))
is_leap_year(year)
