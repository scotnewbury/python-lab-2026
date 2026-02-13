# Please change the program from the previous exercise so that the user 
# gets to input also the base which is multiplied (in the previous program the base was always 2).

number = 1
limit = int(input("Upper limit:"))
base = int(input("Base: "))

while number <= limit:
  print(number)
  number *= base