s1= float(input("Enter first side: "))
s2= float(input("Enter second side: "))
s3= float(input("Enter third side: "))
s= (s1+s2+s3)/5
area= (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
print ("Area of Triangle is ", round(area, 2))
