# EXTRA 1
# Last Digit of Number
# num = input("Number: ")

# lastDigit = int(num[len(num) - 1])

# isLastDigitEven = lastDigit % 2 == 0

# if isLastDigitEven:
#     print("Last digit of {} is even".format(num))

# else:
#     print("Last digit of {} is odd".format(num))



# EXTRA 4
# Magical Date

# month = int(input("Month: "))
# day = int(input("Day: "))
# year = int(input("Year (2 digit): "))

# if month * day == year:
#     print("The date is magical")

# else:
#     print("The date is not magical")



# EXTRA 5
# 1 dollar game
# penniesCount = int(input("Pennies Count: "))
# nickelsCount = int(input("Nickels Count: "))
# dimesCount = int(input("Dimes Count: "))
# quertersCount = int(input("Quarters Count: "))

# total = penniesCount + nickelsCount * 5 + dimesCount * 10 + quertersCount * 25

# if total == 100:
#     print("Congartulations, you made 1 dollar")

# else:
#     if(total > 100):
#         print("More than 1 dollar ({})".format(total))
#     else:
#         print("Less than 1 dollar ({})".format(total))

# EXTRA 7
# Restaurant Selection

# isAnyoneVegan = input("Is anyone vegan (Y/N)?: ") == "Y"
# isAnyoneVegetarian = input("Is anyone vegetarian (Y/N)?: ") == "Y"
# isAnyoneGlutenFree = input("Is anyone gluten-free (Y/N)?: ") == "Y"

# class Restaurant:
#     def __init__(self, name, vegetarian, vegan, gluten):
#         self.name = name
#         self.gluten = gluten
#         self.vegan = vegan
#         self.vegetarian = vegetarian
    

# restaurants = []

# restaurants.append(Restaurant("Joe's Gourmet Burgers", False, False, False))
# restaurants.append(Restaurant("Main Street Pizza Company", True, False, True))
# restaurants.append(Restaurant("Corner Cafe", True, True, True))
# restaurants.append(Restaurant("Mama's Fine Italian", True, False, False))
# restaurants.append(Restaurant("The Chef's Kitchen", True, True, True))

# acceptiableRestaurants = []

# for x in range(0, len(restaurants)):
#     canAcceptiable = True
#     restaurant = restaurants[x]

#     # print(isAnyoneGlutenFree, restaurant.gluten)
#     # print(isAnyoneVegan, restaurant.vegan)
#     # print(isAnyoneVegetarian, restaurant.vegetarian)
#     # print(" ")

#     if((isAnyoneGlutenFree & (restaurant.gluten == False)) | (isAnyoneVegan & (restaurant.vegan == False)) | (isAnyoneVegetarian & (restaurant.vegetarian == False))):
#         canAcceptiable = False    

#     if(canAcceptiable):
#         acceptiableRestaurants.append(restaurant.name)

# print("")

# if(len(acceptiableRestaurants) > 0):
#     print("You can go this restaurants: \n")
#     for i in range(0, len(acceptiableRestaurants)):
#         print("-", acceptiableRestaurants[i])

# else: 
#     print("Non of them is suitable for you!")

# EXTRA 8
# Leap Year

# year = int(input("Year: "))

# isLeapYear = False

# if year % 100 == 0:
#     if(year % 400 == 0):
#         isLeapYear = True

# elif (year % 4 == 0):
#     isLeapYear = True

# if(isLeapYear):
#     print("{} is a leap year & February is 29 days".format(year))
# else:
#     print("{} is not a leap year & February is 28 days".format(year))


# GIVEN SECONDS FORMATTED
sec = int(input("Seconds: "))

oneMinute = 60
oneHour = oneMinute * 60
oneDay = oneHour * 24

seconds = sec % 60
minutes = int((sec % oneHour) / 60)
hour = int((sec % oneDay) / oneHour)
day = int((sec / oneDay))

array = [day, hour, minutes, seconds]

output = ""

if(day > 0):
    output += (str(day) + " day(s) ")

if(hour > 0):
    output += (str(hour) + " hour(s) ")

if(minutes > 0):
    output += (str(minutes) + " minute(s) ")

if(seconds > 0):
    output += (str(seconds) + " second(s)")

print(output)