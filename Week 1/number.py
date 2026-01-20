#import the random library
import random

#generates a random number between 1 and 10
number = random.randint(1, 1000000)

if (number % 2):
    print("Number is odd")
else:
    print("Number is even")

print("The number is", number)