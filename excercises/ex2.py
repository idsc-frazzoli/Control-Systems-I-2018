# Write a program that takes as a input a sentence and save to a dictionary the number of digits
# and of characters contained in the sentence. Print the dictionary.
# e.g: Today is 17 September 2018. -> output = {DIGITS: 6, CHARACTERS: 16}

# Hint: you can use the methods isdigit(), isalpha()

count = {"DIGITS": 0, "CHARACTERS": 0}

s = input("Type here your input:\n")

for symbol in s:
    if symbol.isalpha():
        count["CHARACTERS"] += 1
    if symbol.isdigit():
        count["DIGITS"] += 1


print(count)
