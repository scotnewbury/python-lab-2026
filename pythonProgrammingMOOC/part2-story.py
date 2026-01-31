# Part 1
# Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

# Sample output
# Please type in a word: Once
# Please type in a word: upon
# Please type in a word: a
# Please type in a word: time
# Please type in a word: there
# Please type in a word: was
# Please type in a word: a
# Please type in a word: girl
# Please type in a word: end
# Once upon a time there was a girl

words = ""

word = input("Please type in a word: ")

while word != end:
  words = words + " " +  word
  word = input("Please type in a word: ")

print(words)

