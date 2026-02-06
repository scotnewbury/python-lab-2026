# Part 2 - Simple Loops
#
# Please write a program which asks the user for a year, and prints out the next leap year.
#
# Sample output
# Year: 2023
# The next leap year after 2023 is 2024
#
# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:
#
# Sample output
# Year: 2024
# The next leap year after 2024 is 2028

# The course has been focusing on simple loops and utilizing if/else statements while I could continue this
# trend, I opted to accelerate things and start to include functions. In this case I'll be including a 
# function to check if the year entered is a leap year.


# Let's set up a function that returns true if a given year is a leap year
# and false if it isn't
#
# year: integer
# retun: boolean
def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

# Get the year from the user, cast it as an integer
year = int(input("Year: "))
# Set our next leap year variable to the same year
next_leap_year = year

# Let's calulate the next leap year
# Take the modulo 4 of the year, subtract it from 4, add it to the year the user provided 
# nextLeapYear = year + (4 - (year % 4))

# Check if the next_leap_year is a leap year if not, add one and retest
while True:
  if (is_leap_year(next_leap_year) and year != next_leap_year):
    break
  else:
    next_leap_year += 1

# Print the result
print(f"The next leap year after {year} is {next_leap_year}")

# # Did we calucate a vaild Leap Year?
# if isLeapYear(nextLeapYear):
#   # If we did
#   print(f"The next leap year after {year} is {next_leap_year}")
# else:
#   # if we didn't, add four for the next Leap Year
#   print(f"The next leap year after {year} is {next_leap_year+4}")
