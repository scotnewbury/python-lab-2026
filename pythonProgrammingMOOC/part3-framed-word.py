# Please write a program which asks the user for a string and then
# prints out a frame of * characters with the word in the centre. 
# The width of the frame should be 30 characters. 
# You may assume the input string will always fit inside the frame.
#
# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
#
# Sample output
# Word: testing
# ******************************
# *          testing           *
# ******************************
#
# Sample output
# Word: python
# ******************************
# *           python           *
# ******************************

user_word = input("Word: ")
word_length = len (user_word)

spacing = (30 - word_length) // 2 - 1

print ("*" * 30)
if word_length % 2:
  print ("*" + " " * (spacing + 1 ) + user_word + " " * spacing + "*")
else:
  print ("*" + " " * spacing + user_word + " " * spacing + "*")
  # print ("This is the way")
print ("*" * 30)