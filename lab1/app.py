# Exercise 1 - Get name from user

name = input("What is your name?: ")

greeting = "Hello, " + name + "!"

print(greeting)

# Exercise 2 - Guess birth year by age

age = int(input("How old are you?: "))

currentYear = 2023
birthYear = currentYear - age

print("You probably born in " + str(birthYear))

