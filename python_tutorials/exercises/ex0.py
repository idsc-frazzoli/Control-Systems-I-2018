# Print all integers numbers from 0 to 20
# - If a number is divisible by 3 print "Buzz" instead
# - If a number is divisible by 5 print "Fizz" instead
# - If it is divisible by both 3 and 5 print only the number
# All numbers must be printed on a new line, save the output to a text file called "ex0_output.txt"

##############################################
#                  SOLUTION
##############################################

with open("ex0_output.txt", "w") as f:
    for i in range(0, 21):
        if i % 3 == 0:
            string = "Buzz"
            if i % 5 == 0:
                string = str(i)

        elif i % 5 == 0:
            string = "Fizz"

        else:
            string = str(i)

        print(string)
        f.write(string + '\n')  # add new line




