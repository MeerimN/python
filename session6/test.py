movies = {
    "cinema": "Grand Cinema",
    "location": {
        "city": "New York",
        "state": "NY"
    },
    "films": [
        {
            "title": "Inception",
            "director": "Christopher Nolan",
            "rating": 8.8,
            "genres": ["Sci-Fi", "Thriller"],
            "box_office_millions": 829.9,
            "showtimes": ["18:00", "21:00", "00:30"]
        },
        {
            "title": "The Godfather",
            "director": "Francis Ford Coppola",
            "rating": 9.2,
            "genres": ["Crime", "Drama"],
            "box_office_millions": 246.1,
            "showtimes": ["17:00", "20:30"]
        },
        {
            "title": "Jumanji",
            "director": "Joe Johnston",
            "rating": 6.9,
            "genres": ["Adventure", "Comedy"],
            "box_office_millions": 262.8,
            "showtimes": ["15:30", "19:00", "22:30"]
        }
    ]
}

# High Ratings & Earnings
# Print the title and director of all movies with a rating above 7.5 
# and box office earnings above 250 million.
for movie in movies["films"]:
    if movie["rating"] > 7.5 and movie["box_office_millions"] > 250.0:
        print(movie["title"], "-", (movie["director"]), "-", movie["rating"], "-", movie["box_office_millions"])

# Top-Rated Movie
# Find and print the movie with the highest rating.        

print