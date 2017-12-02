def lhs(a,b):
    eq= (a+b)**2
    return eq

def rhs(a,b):
    e=(a**2)+(2*a*b)+(b**2)
    return e

num_a= int(input('Enter first number: '))
num_b= int(input('Enter second number: '))
num1=lhs(num_a,num_b)
num2=rhs(num_a,num_b)
if(num1==num2):
    print("Since L.H.S= {} and R.H.S = {}".format(num1,num2))
    print("Hence proved")
else:
    print("Not proved")