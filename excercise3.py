# Print out the first two performing artists in that list.
# For each of your favourite movies, print out a sentence about when the movie was released. For example:
# Avatar came out in 2009.
# Mean Girls came out in 2004.
# The Matrix came out in 1999.
# Sort and reverse the list of ages of your family. Save it and print it to the screen.
# See if you can sort and reverse the list on one line!
# Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out



from excercise0 import favourite_artists

print("This is the first artist in the list: {}".format(favourite_artists[0]))
print("This is the second artist in the list: {}".format(favourite_artists[1]))

from excercise0 import fav_movie

print("Sky-High came out in {}".format(fav_movie.get('Sky-High')))
print("Shawshank Redemption came out in {}".format(fav_movie.get('Shawshank Redemption')))
print("Lion King came out in {}".format(fav_movie.get('Lion King')))

from excercise0 import friends_age

friends_age.sort()
friends_age.reverse()

print(friends_age)

fav_movie['Beauty and the Beast'] = '1991', '2017'

print(fav_movie)
