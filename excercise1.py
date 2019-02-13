# Print out the list of coin flips.
# Print out the first element of the list of your favourite colours.
# Output the sorted version of the list of your friends and family members' ages.
#
# Add a new baby (0 years old) to the list of your family's ages.
#
# Using the dictionary of movie information, access and print the year of one of the movies.
#
# If you haven't done so recently, now would be a good time to check that your code works and commit once it does.


from excercise0 import heads_coin_flip

print(heads_coin_flip)

from excercise0 import fav_colors

print(fav_colors[0])

from excercise0 import friends_age

friends_age.sort()
print(friends_age)
friends_age.append('0')
print(friends_age)
