# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
# duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program:
# today is a beautiful day almost perfect today is beautiul did I say day ?

# Hint: use input to get the input words list
s = input("Type here your input:\n")
words = [w for w in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
