# Please write a program which asks the user to type in a string and a single character. 
# The program then prints the first three character slice which begins with the character
# specified by the user. You may assume the input string is at least three characters long. 
# The program must print out three characters, or else nothing.

# Pay special attention to when there are less than two characters left in the string after 
# the first occurrence of the character looked for. In that case nothing should be printed out, 
# and there should not be any indexing errors when executing the program.

# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam

# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

# Sample output
# Please type in a word: tomato
# Please type in a character: x

# Sample output
# Please type in a word: python
# Please type in a character: n

# ADDITIONAL INFORMATION FOR ALL SUBSTRING EXERCISE
# Please make an extended version of the previous program, 
# which prints out all the substrings which are at least three characters long, 
# and which begin with the character specified by the user. 

# You may assume the input string is at least three characters long.

# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot

# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

# Hard coded values for testing
# user_string = "mammoth"
# user_character = "m"

user_string = input ("Please type in a word: ")
user_character = input ("Please type in a character: ")


while True:
  index = user_string.find(user_character)
  if index >= 0 and index + 3 <= len(user_string):
    print (user_string[index:index + 3])
    user_string = user_string[index+1:]
  else:
    break
