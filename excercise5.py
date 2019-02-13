# Find the sum total of the population in the dictionary of cities.
# Using your dictionary containing the names of your family and friends with their ages, print out one of two messages for each depending on their age. For example:
# Martha is old.
# Stewart is young.
# Holly is young.
# Print out the last two colours in your list of favourite colours.
# Increase by 1 the age of everyone in your list of ages. Print it out.
# Add two new colours to your list of favourite colours.


from excercise0 import city_population

sum_total = sum(city_population.values())
print(sum_total)


from excercise0 import names_ages
