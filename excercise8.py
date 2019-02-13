# You want to add up your expenses for the year. Create a list of numbers (integers or floats) that represents your expenses, eg:
#
# [250, 7.95, 30.95, 16.50]
#
# Add up the numbers and output the result.
#
# Put this code into a method. The method should take a list as an argument and return the sum of the expenses in the list. Call the method twice with different lists.



expenses = [250, 8.95, 3.25, 300, 25,50]


def my_expenses(expenses):
    total = sum(expenses)
    print(total)

my_total = my_expenses(expenses)
