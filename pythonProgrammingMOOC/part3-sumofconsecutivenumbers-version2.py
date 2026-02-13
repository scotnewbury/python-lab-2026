# Please write a new version of the program in the previous exercise.
# In addition to the result it should also print out the calculation performed:
#
# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

total = 0
count = 1
sum_string = "The consecutive sum: "
limit = int(input("Upper limit: "))

while total < limit:
  if count == 1:
    sum_string += f"{count} "
  else:
    sum_string += f"+ {count} "
  total += count
  count += 1
  

sum_string += f"= {total}"
print(sum_string)
# print(total)
