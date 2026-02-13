# Please write a program which asks the user to type in a limit.
# The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
# until the sum is at least equal to the limit set by the user.

total = 0
count = 1
limit = int(input("Upper limit: "))

while total < limit:
  total += count
  count += 1

print(total)

