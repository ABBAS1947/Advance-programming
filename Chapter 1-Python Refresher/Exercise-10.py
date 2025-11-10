
film = {
    "Title": "Home Alone",
    "Director": "Cris Columbus",
    "Year": 1990,
    "Genre": "American Christmas",
    "Rating": 8.8,
    "Lead Actor": "Macaulay Culkin"
}

#  here we use  for loop to print the dictionary's key and values, until all of them are printed.
print("Film Details:")
print("-" * 40) # this is not necessary just to divide the first output from the rest.
for key, value in film.items():
    print(f"{key}: {value}")