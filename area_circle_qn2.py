def area(r):
    pi=22/7
    return pi*r**2

r= float(input('Enter radius of the circle:'))
print("The area of the circle of radius{0:.3f}is {1:.3f}".format(r,area(r)))