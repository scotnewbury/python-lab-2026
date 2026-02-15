# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which begin with the first character, 
# from the shortest to the longest. Have a look at the example below.

# Sample output
# Please type in a string: test
# t
# te
# tes
# test

user_string = input("Please type in a string: ")

string_index = 1

while string_index <= len(user_string):
  print(user_string[:string_index])
  string_index += 1

