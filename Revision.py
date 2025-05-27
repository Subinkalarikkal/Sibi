# 1 - Write a program to get two integer and a float from user and find the smallest number
# 2 - Write a program to get two float from user and find the largest number
# 3 - Write a program to print the even numbers between 10 and 20
# 4 - Write a program to print the odd numbers 15 and 25
# 5 - Write a program to get a character from user
# 6 - Write a program to get a string from user
# 7 - Write a program to get three float from user and find the smallest number.
# 8 - Ask the user for the number of months, days, hours, minutes, and seconds they spent on an activity (like playing or studying). Calculate the total time in seconds.
# 9 - Write a program to calculate the total cost of movie tickets. Ask the user how many adults and children are going, then multiply by the ticket prices (e.g., $10 for adults, $7 for children).
# 10 - Savings Tracker
# Ask the user to input the amount of money saved daily for 10 days.
#
# -> Calculate the total savings and average savings per day.
# -> Display results based on the average:
#   Average ≥ $20: "Excellent Saver!"
#   Average ≥ $10 and < $20: "Good Savings Habits!"
#   Average < $10: "Save More Consistently!"
# 11 -add a data into set
# 12 - Remove  a data from set
# 13 - Join 2 set using union function
# 14 - Print the common data in two sets
# 15 - Access an item in dictionary
# 16 - Add an item into dictionary
# 17 - Delete an item from dictionary
# 18 - Change an item from dictionary
# 19 - Looping through dictionary
# 20 - Copy the dictionary
# 21 - Write a program to add a data into the tuple
# 22 - Write a program to remove the mango from tuple
# 23 - Write a program to remove the 3rd index data from tuple
# 24 - Write a program to find the sum of even numbers between a range
# 25 - Write a program to create a oops for the following details :
#       -> Classes - 6
#       ->  3 attributes for each class
#        ->  4 object for each class
# 26 - Write a program to show an example for single, multiple and multi - level inheritance
# 27 - Write a program to show an example for polymorphism and encapsulation

#Question1
# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# c = float(input("Enter a float: "))
#
# if a < b and a < c:
#     print("a is the smallest")
# elif b < c and b < a:
#     print("b is the smallest")
# else:
#     print("c is the smallest")


#Question2
# a = float(input("Enter a float"))
# b = float(input("Enter another float"))
#
# if a > b:
#     print("a is the largest")
# else:
#     print("b is the largest")



#Question3
# for i in range(10, 21):
#     if i % 2 == 0:
#         print(i)
# #
#
#
##Question4
# for i in range(15, 26):
#     if i % 2 != 0:
#         print(i)
#

#
##Question5
# ch = input("Enter a character: ")
# print("Character entered:", ch)


#
##Question6
# text = input("Enter a string: ")
# print("String entered:", text)
#
#
##Question7
# a = float(input("Enter the first float: "))
# b = float(input("Enter the second integer: "))
# c = float(input("Enter a float: "))
#
# if a < b and a < c:
#     print("a is the smallest")
# elif b < c and b < a:
#     print("b is the smallest")
# else:
#     print("c is the smallest")
#
##Question8

# months = int(input("Months: ")) * 30 * 24 * 60 * 60
# days = int(input("Days: ")) * 24 * 60 * 60
# hours = int(input("Hours: ")) * 60 * 60
# minutes = int(input("Minutes: ")) * 60
# seconds = int(input("Seconds: "))
#
# total = months + days + hours + minutes + seconds
# print("Total seconds:", total)

# Question9
# adults = int(input("Adults: "))
# children = int(input("Children: "))
#
# total = adults * 10 + children * 7
# print("Total cost: $", total)
#

# Question10
# total = 0
# for i in range(10):
#     amount = float(input("Day " + str(i+1) + " savings: "))
#     total += amount
#
# average = total / 10
# print("Total saved:", total)
# print("Average per day:", average)
#
# if average >= 20:
#     print("Excellent Saver!")
# elif average >= 10:
#     print("Good Savings Habits!")
# else:
#     print("Save More Consistently!")


#Question11
# my_set = set()
# my_set.add("apple")
# print(my_set)


#Question12
# my_set = {"apple", "banana"}
# my_set.remove("banana")
# print(my_set)




