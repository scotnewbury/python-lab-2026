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
  if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True
  else:
      return False

# Get the year from the user, cast it as an integer
year = int(input("Year: "))

# Let's calulate the next leap year
# Take the modulo 4 of the year, subtract it from 4, add it to the year the user provided 
nextLeapYear = year + (4 - (year % 4))

# Did we calucate a vaild Leap Year?
if is_leap_year(nextLeapYear):
  # If we did
  print(f"The next leap year after {year} is {nextLeapYear}")
else:
  # if we didn't, add four for the next Leap Year
  print(f"The next leap year after {year} is {nextLeapYear+4}")
