# Create a dictionary with film data
film = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Science Fiction",
    "Rating": 8.8,
    "Lead Actor": "Leonardo DiCaprio"
}

# Display film details using loop
print("Film Details:")
print("-" * 40)
for key, value in film.items():
    print(f"{key}: {value}")