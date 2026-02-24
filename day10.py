# voting eligibility
age = int(input("Enter the Age\n"))

if age<0:
    print("Enter Correct Age")
elif age>=18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")
