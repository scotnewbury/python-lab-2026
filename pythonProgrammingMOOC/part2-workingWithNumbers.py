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
  number_count = 0

  while True:
    number = int(input("Number: "))
    if number != 0:
      number_count += 1
    else:
      break

print(f"Numbers typed in {number_count}")