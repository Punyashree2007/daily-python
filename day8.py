# simple calculator
print("Simple Calulator")
a = float(input("Enter a value"))
b = float(input("Enter b value"))
print("1. Add")
print("2. Sub")
print("3. Product")
print("4. Division")

q = int(input("enter the choice"))
if q==1:
    print("add=", a+b)
elif q==2:
    print("sub=",a-b)
elif q==3:
    print("Mul=",a*b)
elif q==4:
    if b!=0:
        print("Div=",a/b)
    else:
        print("Division by Zero is not Possible")
else:
    print("Invalid")