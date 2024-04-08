import math

"""
The German mathematician Gottfried Leibniz developed the following method
to approximate the value of Pi:
Pi/4 =  1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/17 + 1/19 - 1/21 . . .
Write a program that allows the user to specify the number of iterations used in
this approximation and that displays the resulting value.
"""

pi = math.pi
leibniz = 'pi/4'
number_of_iterations = int(input("Enter number of iterations: "))
array = []

for i in range(iterations):
    for j in range(3, i, 2):
        array.append(j)

print(f'{leibniz} =  1 - 1/ {array}')