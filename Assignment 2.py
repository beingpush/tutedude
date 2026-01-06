# Check if Numbers are Even or Odd

num = int(input("Enter a Number: "))

if num % 2 == 0:

    print(f"{num} is an Even Number")

else:
    print(f"{num} is an Odd Number")

# Sum of Integers from 1 to 50 Using a Loop

sum = 0

for i in range(1,51):
    sum = sum + i

print(f"The Sum of numbers from 1 to 50 is: {sum}")