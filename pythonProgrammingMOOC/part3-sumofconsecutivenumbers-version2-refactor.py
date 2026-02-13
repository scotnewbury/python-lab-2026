# Refactoring the final exercise in part 3
#
# Please write a new version of the program in the previous exercise.
# In addition to the result it should also print out the calculation performed:
#
# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Grab my function to get an integer from the user
from utility import get_integer_from_user


def main():

  total = 1
  count = 1
  numbers = "1"
  limit = get_integer_from_user("Limit: ")

  while total < limit:
    count += 1
    total += count
    numbers += f" + {count}"
    
    
  print(f"The consecutive sum: {numbers} = {total}")


if __name__ == "__main__":
  main()

