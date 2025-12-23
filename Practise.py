name= "Pushkar"
age= 30
lang= "Python"
s1= "Hello Guys"
s2= "How Are you?"
combine= f"Combine two strings without concatenation using \"f string\", \"{s1}\", \"{s2}\""

print(combine)

s1= "Hello Guys"
s2= "How Are you?"
slicing= s1[0:5:1]

print("Slicing of string by removing \"Guys\" from a string", slicing + ", " + s2)
print(name,"is",age,"years old and learning",lang)

# "f" string

name= "Pushkar"
age= 30
lang= "Python"
sub1= 78
sub2=99
sub3= 89
sub4= 96
Total= sub1 + sub2 + sub3 + sub4

print(f"{name} is {age} years old and learning {lang} and says '{s1}, {s2}'" f" and scored {sub1 + sub2 + sub3 + sub4} out of 400. which is approximately {Total/400*100}%")

# Escape Sequencing

# Escape sequence tab (\t)

print("1. new\told")

# Escape sequence new line (\n)

print("2. new\nold")

# Escape sequence \' 0r \"

print("3. \'new\'\\\'old\'")

# Escape sequence backslash (\\)

print("4. new\\old")

# String operations

#  "in" (Gives "True" if str is there else gives "False") Note: it is case-sensitive, like if you type in Capital like "In" it won't work

s1= "Hello Guys"
s2= "How Are you?"

print(s1)
print(s2)

print("Hello" in s1)
print("How" in s2)
print("Hello" in s2)
print("How" in s1)

#  "not in" (Gives "True" if str is not there else gives "False") Note: it is case-sensitive, like if you type in Capital like "Not In" it won't work

s1= "Hello Guys"
s2= "How Are you?"

print(s1)
print(s2)

print("Hello" not in s2)
print("How" not in s1)
print("Hello" not in s1)
print("How" not in s2)

# String Comparison

s1= "Hello Guys"
s2= "How Are you?"
s3= "Pushkar "
name= "Pushkar"
sub1= 78
sub2=99
sub3= 89
sub4= 96
Total= sub1 + sub2 + sub3 + sub4

print(s1 == s2)
print(Total == sub1 + sub2 + sub3 + sub4)
print(s3 == name) # "False" Because there is a space in s3 in the end.

# Strip function
# Removing space from string "strip()" function removes the space at the start & end of the string.

s3= "Pushkar "
name= "Pushkar"

print(s3.strip())
print(s3.strip() == name)

# Replace function
# Replace part of the string with different another string. "replace" (old value in quote or if variable present then without quote, new value within quote)

s1= "Hello Guys"

print(s1.replace("Guys", "All"))
print(s1.replace("Hello", "Hi"))

# Count function
# Counting of substring in main string which gives you the exact count of substring present in main string.

s4= "Python is amazing and simple language to code in"
lang= "Python"

print(s4.count("Python"))
print(s4.count(lang))
print(f"Occurrences of {lang} in variable s4 is {s4.count(lang)}")


# List

DAYS_IN_WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(f"Last day of the week is \"{DAYS_IN_WEEK[-1]}\".")
print(len(DAYS_IN_WEEK))

# Slicing of list

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(L1[1:8:2]) #1 is to start in a list, 8 is to end in a list, 2 is to print / skip the index value.

#Concatenation of list

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(L1 + L2)

# "*" Repetition of strings

L1 = [1, 2, 3]

print(L1 * 2)

# Append Function
# To add Single value in List

Name = ["Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.append("Bharat")

print(Name)

# Insert Function
# To add value at specified index, Note: It takes first argument as index number & second arguments as the value to be added.

Name = ["Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.insert(1, "Bharat")

print(Name)

# Extend Function
# Just like append but in append you can only add single value, but in extend you can add multiple values.

Name = ["Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.extend(["Bharat", "Chandrakant"])

print(Name)

# Remove Function
# To remove value from list, Note: it only deletes first occurrence of the value.
Name = ["Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.remove("Pushkar")

print(Name)

# Pop FUnction
# TO remove value from list at specific index, Note: it only takes index number as argument and if no argument is provided it will delete last index of the list.

Name = ["Pushkar", "Manjusha", "Surbhi", "Chandrakant", "Bharat", "Chandrakant"]

Final_Name = Name.pop(5)

print(Name)

# Reverse function
# To reverse values in list in descending order.

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Final_DAYS_IN_WEEK = DAYS_IN_WEEK.reverse()

print(DAYS_IN_WEEK)

# Sort function
# To sort list in required order. Note: if no arguments are provided it will sort in ascending order.

DAYS_IN_WEEK = [9, 4, 3, 2, 5, 8, 7, 6, 1, 10]

Final_DAYS_IN_WEEK = DAYS_IN_WEEK.sort()

print(DAYS_IN_WEEK)

FINAL_DAYS_IN_WEEK = DAYS_IN_WEEK.sort(reverse=True)

print(DAYS_IN_WEEK)

# Count function
# To count particular value in list.

DAYS_IN_WEEK = [9, 4, 3, 2, 5, 8, 7, 6, 1, 10, 2, 4, 7, 4, 4, 2, 3, 4,  6, 3, 2]

Num = int(input("Enter the number to count: "))

Result = DAYS_IN_WEEK.count(Num)

Final_output = (f"Occurrences of {Num} is {Result}")

print(Final_output)

# Min function
# To check the Smallest value in given list.

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Smallest Number in list is: {min(DAYS_IN_WEEK)}")

# Max function
# To check the Largest value in given list.

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Largest Number in list is: {max(DAYS_IN_WEEK)}")

# Sum function
# To check the sum of values in given list.

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"The sum of values in list is: {sum(DAYS_IN_WEEK)}")

# Nested list
# To fetch nested list values.

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, [1, 2, 3], 9, 10]

print(DAYS_IN_WEEK[-3][0])

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, [1, 2, 3, [2, 3, 4, 5, [1, "Pushkar", 3, 4]]], 9, 10]

print(DAYS_IN_WEEK[-3][-1][-1][-3])











