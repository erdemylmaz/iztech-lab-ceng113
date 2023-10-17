# # EXERCISE 1 ---------------------------------------------------------------------------------
# # Calculate absolute value of given number

# number = int(input("Number: "))

# absNumber = number

# if number < 0:
#     absNumber = -1 * number

# output1 = "Absolute value of " + str(number) + " is: " + str(absNumber)

# print(output1)



# # EXERCISE 2 ---------------------------------------------------------------------------------
# # Calculate minimum of given 3 number

# num1 = int(input("What is n1: "))
# num2 = int(input("What is n2: "))
# num3 = int(input("What is n3: "))

# minimumNumber = num1

# if(num2 < minimumNumber):
#     minimumNumber = num2
# elif (num3 < minimumNumber):
#     minimumNumber = num3

# output2 = "Minimum number of [" + str(num1) + ", " + str(num2) + ", " + str(num3) + "] is: " + str(minimumNumber)

# print(output2)



# # EXERCISE 3 ---------------------------------------------------------------------------------
# # GPA & Lesson

# gpa = int(input("GPA: "))
# lessonCount = int(input("Number of Lessons: "))

# if gpa < 2 & lessonCount < 47:
#     print("Not enough number of lectures and GPA!")

# elif gpa >= 2 & lessonCount < 47:
#     print("Not enough number of lectures!")

# elif gpa >= 2 & lessonCount >= 47:
#     print("GRADUATED!!!")

# elif gpa < 2 & lessonCount >= 47:
#     print("Not enough GPA!")

# else:
#     print("Please give correct information!")



# # EXERCISE 4 ---------------------------------------------------------------------------------
# # Age & Ticket Price

# TICKET_PRICE = 3
# age = int(input("How old are you?: "))

# if age > 60 | age < 6:
#     TICKET_PRICE = 0

#     print("Ticket Price is:", TICKET_PRICE)

# elif age >= 6 & age <= 18:
#     TICKET_PRICE = TICKET_PRICE * 0.5

#     print("Ticket Price is:", TICKET_PRICE)

# elif age < 0:
#     print("Please give correct age information")



# # EXERCISE 5 ---------------------------------------------------------------------------------
# # Quadric Equation

# print("\nax^2 + bx + c \n")

# a = int(input("What is a?: "))
# b = int(input("What is b?: "))
# c = int(input("What is c?: "))

# discriminant = (b ** 2) - (4 * a * c)

# root1 = (-1 * b + (discriminant ** 1/2)) / 2 * a
# root2 = (-1 * b - (discriminant ** 1/2)) / 2 * a

# if discriminant > 0:
#     print("It has 2 roots and they are: " + str(root1) + " and " + str(root2))

# elif discriminant == 0:
#     print("It has 1 root and it is: " + str(root1))

# else:
#     print("There are no real roots!")



# # EXERCISE 6 ---------------------------------------------------------------------------------
# # Turtle

# from turtle import *

# size = int(input("Shape Count: "))

# stepSize = 80 - size * 2

# if size <= 40:
#     deg = 360 / size

#     while size > 0:
#         size -= 1
#         forward(stepSize)
#         right(deg)
        
# else:
#     circle(32)