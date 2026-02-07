# Pre-task
# Please write a program which asks the user for integer numbers. 
# The program should keep asking for numbers until the user types in zero.

# Sample output
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

print ("Please type in integer numbers. Type in 0 to finish.")

if __name__ == "__main__":
  number = 0
  number_count = 0
  positive = 0
  negative = 0
  mean = 0
  sum = 0

  while True:
    number = int(input("Number: "))
    if number != 0:
      number_count += 1
      sum = sum + number
      if number > 0:
        positive += 1
      else:
        negative += 1
    else:
      break
  mean = sum / number_count
  print(f"Numbers typed in {number_count}")
  print(f"The sum of the numbers is {sum}")
  print(f"The mean of the numbers is {mean}")
  print(f"Positive numbers {positive}")
  print(f"Negative numbers {negative}")