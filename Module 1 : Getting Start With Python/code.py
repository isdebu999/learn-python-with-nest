# Student Details
roll = 101
name = "Raj"
stream = "Computer Science"
cgpa = 9.2

print("Roll Number: " + str(roll))
print("Name: " + name)
print("Stream: " + stream)
print("CGPA: " + str(cgpa))


# Greeting
name = "Raj!"
print("Hello, " + name)


# Book Details
title = "The Alchemist"
author = "Paulo Coelho"
publisher = "HarperOne"
price = 299.99

print("Title: " + title)
print("Author: " + author)
print("Publisher: " + publisher)
print("Price: " + str(price))


# Movie Details
movie_title = "Inception"
director = "Christopher Nolan"
release_year = 2010
rating = 8.8

print("Movie Title: " + movie_title)
print("Director: " + director)
print("Release Year: " + str(release_year))
print("Rating: " + str(rating))


# Addition
num1 = 15
num2 = 30
res = num1 + num2

print("The sum of " + str(num1) + " and " + str(num2) + " is: " + str(res))


# Subtraction
num1 = 50
num2 = 20
difference_result = num1 - num2

print("The difference between " + str(num1) + " and " + str(num2) + " is: " + str(difference_result))


# All Arithmetic Operations
num1 = 12
num2 = 4

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference between {num1} and {num2} is: {difference_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
print(f"The quotient when {num1} is divided by {num2} is: {quotient_result}")


# Rectangle Area and Perimeter
length = 7.5
width = 3.2

area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle with length {length} and width {width} is: {area}")
print(f"The perimeter of the rectangle with length {length} and width {width} is: {perimeter}")


# Uppercase Conversion
message = "python programming is interesting"
new_message = message.upper()

print(new_message)


# Temperature Conversion
cel_tem = 36.6
faren_tem = round((cel_tem * 9/5) + 32, 2)

print(f"The temperature {cel_tem} deg C is equivalent to {faren_tem} deg F")


# Strip Whitespace
message = "  Python is amazing!  "
new_message = message.strip()

print(new_message)