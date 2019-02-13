# Print out all of the ages of your friends/family that are less than 30 (or any number where some ages will not be printed!).
# Find and output the age of the oldest person in your friends/family list.
# Count how many times you flipped 'heads' using the coin flips list.
# You realize one of the performing artists in your list is no longer a favourite. Remove one of them from the list.
# Pick a city in your city population dictionary and change its population.


from excercise0 import friends_age

for age in friends_age:
    if (age > 30):
        print("Prints nothing")
    elif (age < 30):
        print(age)


print("The oldest age in the list is:",max(friends_age))

from excercise0 import heads_coin_flip

count = 0
for heads in heads_coin_flip:
    if (heads == 'yes'):
        count += 1
        print("The flip was heads count will go up by 1")
        print(count)
    elif (heads == 'no'):
        print("The result was tails, count will stay at what it is")


from excercise0 import favourite_artists

favourite_artists.remove('Kanye West')
print(favourite_artists)

from excercise0 import city_population
city_population['New York'] = '0'

print(city_population)
