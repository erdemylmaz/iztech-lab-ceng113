# Exercise 1
# factorial

# isNonNegative = False

# while isNonNegative == False:
#     number = int(input("Number [non-negative]: "))

#     if(number >= 0):
#         isNonNegative = True

# result = 1

# for x in range(1, number + 1):
#     if(x != 0):
#         result *= x
    

# output = "Factorial of " + str(number) + " is: " + str(result)

# print(output)



# Exercise 2
# Prime numbers between 2 int

# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))

# min = num1
# max = num2

# if(num2 < num1):
#     min = num2
#     max = num1

# primeNumbers = []

# for x in range (min + 1, max):
#     isPrime = True
#     for controlNumber in range(2, x):
#         if(x % controlNumber == 0):
#             isPrime = False
#             break
#     if(isPrime):
#         primeNumbers.append(x)
    
# print(primeNumbers)

# Exercise 3
# Star

# isOdd = False

# while isOdd == False:
#     number = int(input("Odd Number: "))

#     if(number % 2 == 1):
#         isOdd = True

# # PRINT TOP
# for x in range(1, number + 1, 2):
#     spaceCount = int((number - 1 / 2) - (x + 1) / 2)
#     print(" " * spaceCount + x * "*")

# # PRINT BOT
# for x in range(number - 2, 0, -2):
#     spaceCount = int((number - 1 / 2) - (x + 1) / 2)
#     print(" " * spaceCount + x * "*")



# Exercise 4
# Guess the number
# import random

# randomNumber = random.randint(1, 20) 

# number = int(input("Guess the number 1-20: "))

# guessCount = 1

# isInInterval = 1 <= number <= 20

# while isInInterval == False:
#     number = int(input("Please, guess the number between 1 to 20: "))

#     if(1 <= number <= 20):
#         isInInterval = True

# isCorrect = number == randomNumber

# while isCorrect != True:
#     number = int(input("Wrong, try again! Guess the number between 1 to 20: "))

#     isInInterval = 1 <= number <= 20

#     while isInInterval == False:
#         number = int(input("Please, guess the number between 1 to 20: "))

#         if(1 <= number <= 20):
#             isInInterval = True

#     guessCount += 1

#     if(number == randomNumber):
#         isCorrect = True
#         break


# print("YOU WON IN {} GUESS!".format(guessCount))




# Exercise 5
# Turtle Hexagon
