# Make a new dictionary that contains a list of movies for each year. Each list of movies should be a list. Below is some data you can use.
#
# 1999: The Matrix, Star Wars: Episode 1, The Mummy
# 2009: Avatar, Star Trek, District 9
# 2019: How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9
# Make a new list that contains each row of the buttons on a phone. Each row should be a list.
#
# The rows on a phone are: 1 2 3, 4 5 6, 7 8 9, * 0 #
# Make a new list that contains information about three countries. Each country should be a dictionary that has a name, a continent, and whether or not it is an island.


movie_dates = {1999: ['The Matrix', 'The Phantom Menace', 'The Mummy'],
                2009: ['Inglorius Bastards', 'Avatar', 'District 9'],
                2019: ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']}

print(movie_dates)


phone_rows = ['123', '456', '789', '*0#']

print(phone_rows)

country_info = [ {'Madagascar':'Africa', 'island':'Yes'},
                 {'Zimbabwe':'Africa', 'island':'No'},
                 {'Germany':'Europe', 'island':'No'} ]

print(country_info)
