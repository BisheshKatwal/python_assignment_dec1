def far_to_cel(F):
    C = (F - 32) * 5.0 / 9.0
    return C

def cel_to_far(C):
    F=(9.0/5.0) * C + 32
    return F

num=int(input("enter 1 for fahrenheit to celsius conversion or 2 for celsius to fahrenheit conversion: "))
if(num==1):
    F=float(input('Enter the temperature in Fahrenheit: '))
    print('The corresponding temperature in celsius is {0:.2f}'.format(far_to_cel(F)))
elif(num==2):
    C=float(input('Enter the temperature in Celsius: '))
    print('The corresponding temperature in fahrenheit is {0:.2f}'.format(cel_to_far(C)))
else:
    print("Invalid input")