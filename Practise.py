from IPython.core.inputtransformer2 import TokenTransformBase
from parso.python.tokenize import PythonToken

s1= "Hello Guys"
s2= "How Are you?"
name= "Pushkar"
age= 30
lang= "Python"
sub1= 78
sub2=99
sub3= 89
sub4= 96
Total= sub1 + sub2 + sub3 + sub4

combine= f"{s1}, {s2}"

print(combine)

slicing= s1[0:5:1]

print(slicing + ", " + s2)

print(name,"is",age,"years old and learning",lang)

#fstring

print(f"{name} is {age} years old and learning {lang} and says '{s1}, {s2}'" f" and scored {sub1 + sub2 + sub3 + sub4} out of 400. which is approximately {Total/400*100}%")

#Escape Sequencing

#Escape sequence tab (\t)

print("1 new\told")

#Escape sequence new line (\n)

print("2 new\nold")

#Escape sequence \' 0r \"

print("3 \'new\'\\\'old\'")

#Escape sequence backslash (\\)

print("4 new\\old")

#string operations

#  "in" (Gives "True" if str is there else gives "False") Note: it is case sensitive, like if you type in Capital like "In" it won't work

print(s1)
print(s2)

print("Hello" in s1)
print("How" in s2)
print("Hello" in s2)
print("How" in s1)

#  "not in" (Gives "True" if str is not there else gives "False") Note: it is case sensitive, like if you type in Capital like "Not In" it won't work

print(s1)
print(s2)

print("Hello" not in s2)
print("How" not in s1)
print("Hello" not in s1)
print("How" not in s2)









