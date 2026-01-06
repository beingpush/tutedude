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

print(f"Slicing of string by removing \"Guys\" from a string s1 and concatenating with string s2","\n",slicing + ", " + s2)

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

print("1. Escape Sequence character tab,\nnew\told")

# Escape sequence new line (\n)

print("2. Escape Sequence character New Line, \nnew\nold")

# Escape sequence \' 0r \"

print("3. Escape Sequence character for Comma, \n\'new\'\\\'old\'")

# Escape sequence backslash (\\)

print("4. Escape Sequence character for back slash, \nnew\\old")

# String operations

#  "in" (Gives "True" if str is there else gives "False") Note: it is case-sensitive, like if you type in Capital like "In" it won't work

s1= "Hello Guys"
s2= "How Are you?"

print("Hello" in s1)
print("How" in s2)
print("Hello" in s2)
print("How" in s1)

#  "not in" (Gives "True" if str is not there else gives "False") Note: it is case-sensitive, like if you type in Capital like "Not In" it won't work

s1= "Hello Guys"
s2= "How Are you?"

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
#Only works on strings and not on list or tuple.

s1= "Hello Guys"
t1 = [1, 2, 3, 4]

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

# Replace value in list.

t1 = ["Replace", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t1[-2] = 11

print(t1)

# Append Function in list
# To add Single value in List

Name = ["Append", "Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.append("Bharat")

print(Name)

# Insert Function in list
# To add value at specified index, Note: It takes first argument as index number & second arguments as the value to be added.

Name = ["Insert", "Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.insert(1, "Bharat")

print(Name)

# Extend Function in list
# Just like append but in append you can only add single value, but in extend you can add multiple values.

Name = ["Extend", "Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.extend(["Bharat", "Chandrakant"])

print(Name)

# Remove Function
# To remove value from list, Note: it only deletes first occurrence of the value.
Name = ["Remove", "Pushkar", "Manjusha", "Surbhi"]

Final_Name = Name.remove("Pushkar")

print(Name)

# Pop Function in list
# TO remove value from list at specific index, Note: it only takes index number as argument and if no argument is provided it will delete last index of the list.

Name = ["Pop", "Pushkar", "Manjusha", "Surbhi", "Chandrakant", "Bharat", "Chandrakant"]

Final_Name = Name.pop(5)

print(Name)

# Reverse function in list
# To reverse values in list in descending order.

DAYS_IN_WEEK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Final_DAYS_IN_WEEK = DAYS_IN_WEEK.reverse()

print(DAYS_IN_WEEK)

# Sort function in list
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

# Tuple
# We can not modify the Tuple as in list does. Note: Parenthesis are optional i.e. ()

DAYS_IN_WEEK = (1, 2, 3, 4, 5, 6, 7, [1, 2, 3], 9, 10)

print(DAYS_IN_WEEK[0])

DAYS_IN_WEEK = 1, 2, 3, 4, 5, 6, 7, [1, 2, 3], 9, 10, "Pushkar" #No Parenthesis are given i.e. ()

print(type(DAYS_IN_WEEK))

print(DAYS_IN_WEEK[-4][-2])

s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(s1, type(s1))

t1 = tuple(s1)

print(t1, type(t1))

# Operations on Tuples

#Concatenation in Tuple

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = (11, 12, 13, "Pushkar", "Surbhi")

T = t1 + t2

print(T)

# "*" in Tuple

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = (11, 12, 13)

T = t2 * 4

print(T)

# in / not in

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = (11, 12, 13, "Pushkar", "Surbhi")

T = 12 in t2

S = 12 not in t2

print(T)
print(S)

# Index of a value in Tuple

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(t1.index(4))

# Sets
# Same as List but the sets does not print values which are repetitive. Note: You can not access specific index value in sets.

t1 = {"Does Not repeat the value and does not print the values in sequence (refer output to understand)", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 1}

print(t1)

print(2 in t1)

# Intersection / & Function in Sets.
# Common value in multiple different sets.

t1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
t2 = {1, 7, 5, 8, 9, 10}
t3 = {1, 2, 3, 4, 5}

print(t1.intersection(t2, t3))

# Union / | Function in Sets.
# To add values of multiple sets and print it without repetition.

t1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
t2 = {11, 12, 13, "Pushkar", "Surbhi"}
t3 = {21, 22}

print(t1.union(t2, t3))
print(t1 | t2 | t3)


# Difference / - Function in Sets.
# To find difference between multiple Sets.

t1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
t2 = {1, 2, 3, 11, 12, 13, "Pushkar", "Surbhi"}
t3 = {21, 22, "Pushkar", "Surbhi"}

print(t1.difference(t2, t3))
print(t1 - t2, t1 - t3)

# Dictionaries. Note: Dict are mutable.

Dict = {"Food":"Apple", "Sweet":"Jamun", "Food":"Banana"}

print(Dict["Food"])

Dict["Food"] = "Mango" # This will add / update the key to the Dict.

print(Dict)

# get Function
# To fetch the value of particular key from dict. Note: this has 2 arguments like if there is no key present in dict you can provide desired value by putting comma after 1st argument.

Dict = {"Food":"Apple", "Sweet":"Jamun"}

print(Dict.get("Food"))

print(Dict.get("Spice", "Mirchi")) # To fetch desired value if key is not present in dict.

# update Function
# To update one dict with another.

Dict1 = {"Food":"Apple", "Sweet":"Jamun"}
Dict2 = {"Veggies":"Cabbage", "Spice":"Mirchi", "Food":"Banana"}

Dict1.update(Dict2)

print(Dict1)

# pop Function.
# To remove key from dict.

Dict1 = {"Food":"Apple", "Sweet":"Jamun"}

Dict1.pop("Food")

print(Dict1)

# keys Function
# To fetch all present Keys in dict.

Dict1 = {"Food":"Apple", "Sweet":"Jamun"}

print(Dict1.keys())

# values Function.
# To fetch all present Values in dict.

Dict1 = {"Food":"Apple", "Sweet":"Jamun"}

print(Dict1.values())

# items Function.
# To fetch all present key value pairs in dict.

Dict1 = {"Food":"Apple", "Sweet":"Jamun"}

print(Dict1.items())

# for loop

age = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in age:
    print(i)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# if statement

Dict1 = str(input("Enter a Item: "))

if "Food" or "Sweet" in Dict1:

    print("Item is present in dictionary")

# if-else statement

Num = int(input("Enter a Number: "))

if Num >= 0:

    print("The Number is positive")

else:
    print("The Number is negative")

# elif statement

Marks = float(input("Enter a Marks: "))

if Marks == 100:
    print("The Student got out of marks")

elif Marks < 100 and Marks >= 85:
    print("The Student got A Grade")

elif Marks < 85 and Marks >= 75:
    print("The Student got B Grade")

elif Marks < 75 and Marks >= 55:
    print("The Student got C Grade")

elif Marks < 55 and Marks >= 35:
    print("The Student got D Grade")

else:
    print("The Student is failed")

# Nested if statement

Marks = float(input("Enter a Marks: "))

if Marks > 35:

    if Marks == 100:
        print("The Student got out of marks")

    if Marks < 100 and Marks >= 85:
        print("The Student got A Grade")

    if Marks < 85 and Marks >= 75:
        print("The Student got B Grade")

    if Marks < 75 and Marks >= 55:
        print("The Student got C Grade")

    if Marks < 55 and Marks >= 35:
        print("The Student got D Grade")

else:
    print("The Student is failed")




