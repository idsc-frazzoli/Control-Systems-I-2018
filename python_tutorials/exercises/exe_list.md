## Summary
Recap of the proposed exercises.

### Exercise #0
Print all integers numbers from 0 to 20
 - If a number is divisible by 3 print "Buzz" instead
 - If a number is divisible by 5 print "Fizz" instead
 - If it is divisible by both 3 and 5 print only the number.
 
 All numbers must be printed on a new line. Save the output to a text file called "ex0_output.txt"

### Exercise #1
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program:

_today is a beautiful day almost perfect today is beautiful did I say day ?_

**Hint**: use `input("prompt string")` to get the input words list from terminal.

### Exercise #2
Write a program that takes as a input a sentence and save to a dictionary the number of digits
and of characters contained in the sentence. Print the dictionary.
e.g: 
- Input: _Today is 17 September 2018._ 
- Output: `{DIGITS: 6, CHARACTERS: 16}`

**Hint**: you can use the methods `isdigit()`, `isalpha()`

### Exercise #3
Write a binary function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.

_Binary search_ works looking at the middle element of the list and takes the left or right half
if the item is less or greater then the middle element respectively. The procedure is then repeated until the element is
found.

**Hint**: `import math` for the `floor()` and `ceil()` functions.

### Exercise #4

Compare solution ode euler method and odeint

ODE problems are important in computational physics, so we will look at one more example: the damped harmonic
oscillation. This problem is well described on the wiki page: http://en.wikipedia.org/wiki/Damping

The equation of motion for the damped oscillator is:

xdd+2\*zeta\*omega_0\*xd+omega_0^2\*x=0

where  x  is the position of the oscillator,  ω0  is the frequency, and  ζ  is the damping ratio.
To write this second-order ODE on standard form we introduce  
x_1=x and x_2 = dx:

dx_1=x_2

dx_2=−2\*zeta\*omega_0\*x_2−omega_0^2\*x_1

In the implementation of this example we will add extra arguments to the RHS function for the ODE,
rather than using global variables as we did in the previous example.
As a consequence of the extra arguments to the RHS, we need to pass an keyword argument args to the odeint function:

Then we compare solution to the first order Euler discretization.
