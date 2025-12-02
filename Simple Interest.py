P= float(input("Enter Principle Amount: "))
R= float(input("Enter Rate of Interest: "))
T= float(input("Enter Tenure: "))

SI=(P*R*T)/100

A = SI + P

print("The Interest is: ", SI)
print("Total Amount is: ", A)

