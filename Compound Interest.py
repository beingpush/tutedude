P= float(input("Enter Principle Amount: "))
R= float(input("Enter Rate of Interest: "))
T= float(input("Enter Tenure: "))

B= (1 + R/100)

A= P * pow(B, T)

CI = A - P

print("The CI is: ", round(CI, 2))
print("The Amount is: ", round(A, 2))

