# Pre-task
# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

# Sample output
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

# Part 1: Count
# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4

# Part 2: total
# The program should also print out the total of all the numbers typed in. The zero at the end should not be included in the calculation.

# The program should now print out the following:

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The total of the numbers is 34

# Part 3: Mean
# The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The tota1 of the numbers is 34
# The mean of the numbers is 8.5

# Part 4: Positives and negatives
# The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The tota1 of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1

from utility import get_integer_from_user

print ("Please type in integer numbers. Type in 0 or just hit enter to finish.")

number = 0
number_count = 0
positive = 0
total = 0

while True:
  # Get an integer from the user, check for valid input
  number = get_integer_from_user("Number: ")

  if number == 0:
    break
    number_count += 1
    total = total + number
    if number > 0:
      positive += 1

print(f"Numbers typed in {number_count}")
print(f"The total of the numbers is {total}")

if number_count:
  print(f"The mean of the numbers is {total / number_count}")
else:
  print("Cannot calculate mean, division by zero.")

print(f"Positive numbers {positive}")
print(f"Negative numbers {number_count - positive}")