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

from utility import is_leap_year

# Get the year from the user, cast it as an integer
while True:
  try:
    year = int(input("Year: "))
    break  # Exit loop, entry valid
  except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Set our next leap year variable one more than the current year to start the loopo
next_leap_year = year + 1

# Determine the next leap year
while True:
  if (is_leap_year(next_leap_year)):
    break
  else:
    next_leap_year += 1

# Print the result
print(f"The next leap year after {year} is {next_leap_year}")
