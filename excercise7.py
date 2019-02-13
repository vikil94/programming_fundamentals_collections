# Output the message "I will not skateboard in the halls" 20 times.
#
# Create a list consisting of the above message. It should appear in the list 20 times.
#
# Create a list consisting of the numbers between 1 and 50.
#
# Use a for loop to find the sum of the numbers in the above list.
#
# Create a new list which has three of each number up to 50.
#
# Ie. [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50] and so on, up to 50.
# Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands. Print out both lists.
from excercise6 import country_info

for i in range(0,20):
    print("I will not skateboard in the halls")


list_appear = ["It should appear 20 times"]

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
43, 44, 45, 46, 47, 48, 49, 50]

print(list_numbers)

print(sum(i for i in list_numbers))

new_list = []
for number in range(1,51):
    new_list.append(number)
    new_list.append(number)
    new_list.append(number)

print(new_list)

non_islands = []
islands = []
for each_country in country_info:
    if each_country['island']:
        islands.append(each_country['name'])
    elif not each_country['island']:
        non_islands.append(each_country['name'])

print('The list of non-islands is {}'.format(non_islands))
print('The list of islands is {}'.format(islands))
