# create a variable called color with an appropriate value on the line below, remember, strings in Python must be enclosed in 'single' or "double" quotes)
color = "blue"

pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter/2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * radius * radius

a = [1, 2, 3]
b = [3, 2, 1]
# to change values of a to b
a_swap = a
b_swap = b
a = b_swap
b = a_swap

# make the result 1
result = (5 - 3) // 2
print(result)

# Add parentheses to the following expression so that it evaluates to 0.
result_2 = 8 - (3 * 2) - (1 + 1)
print(result_2)

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3
print(to_smash)
