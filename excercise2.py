# Print out the last element of the list of your favourite colours.
# Note: do this in a way that would still work for a list of any size!
# Add a new city to the dictionary of cities and population.
# Reverse the list of coin flips and save it.
# Print out the population of one of the cities.
# Print out a sentence about each item in the list of performing artists. For example:
# I think Pearl Jam is great.
# I think Lady Gaga is great.
# I think Pink Floyd is great.


from excercise0 import fav_colors

# -1 will always get the last element in your list
print("The last element in the list {}".format(fav_colors[-1]))

from excercise0 import city_population
# this will add a new item to your dictionary
city_population['New York'] = '8.623 million'
print(city_population)

from excercise0 import heads_coin_flip

heads_coin_flip.reverse()
print(heads_coin_flip)

# this will print out Toronto's population
print(city_population.get('Toronto'))

from excercise0 import favourite_artists

print("I think {} is great".format(favourite_artists[0]))
print("I think {} is awesome".format(favourite_artists[1]))
print("I think {} is cool".format(favourite_artists[2]))
