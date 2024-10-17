# WRITE YOUR CODE HERE

# Reuse the array

favourite_movies = [
    {
        "title": "Kill Bill",
        "year": 2003,
        "rating": 8.2,
        "directors": ["Quentin Tarantino"],
        "writers": ["Quentin Tarantino"],
        "actors": ["Uma Thurman", "Lucy Liu", "David Carradine"],
        "genres": ["Action", "Comedy", "Drama"],
        "description": "A pregnant assassin, code-named The Bride, goes into a coma for four years after her ex-boss Bill brutally attacks her. When she wakes up, she sets out to seek revenge on him and his associates.",
        "is_published_after_2000": True
    },
    {
        "title": "Matrix",
        "year": 1999,
        "rating": 8.7,
        "directors": ["Lana Wachowski", "Lilly Wachowski"],
        "writers": ["Lana Wachowski", "Lilly Wachowski"],
        "actors": ["Keanu Reeves", "Carrie-Anne Moss", "Laurence Fishburne"],
        "genres": ["Action", "Noir", "Drama"],
        "description": "Neo, a computer programmer and hacker, has always questioned the reality of the world around him. His suspicions are confirmed when Morpheus, a rebel leader, contacts him and reveals the truth to him.",
        "is_published_after_2000": False
    }
]

# Display authors using 'for' loop

for movie in favourite_movies:
    print(movie["title"]) 
for movie in favourite_movies:
    print(movie["directors"]) 

# Check the age of books using 'if'
# Check the age of books using 'if/else'

if favourite_movies[0]["is_published_after_2000"] == True:
    print("This movie is newer than 2000:", favourite_movies[0]["title"])
else:
    print("This movie is older than 2000:", favourite_movies[0]["title"])

if favourite_movies[1]["is_published_after_2000"] == True:
    print("This movie is newer than 2000:", favourite_movies[1]["title"])
else:
    print("This movie is older than 2000:", favourite_movies[1]["title"])

# Check the age of books switched

if favourite_movies[0]["is_published_after_2000"] != True:
    print("This movie is newer than 2000:", favourite_movies[0]['title'])
else:
    print("This movie is older than 2000:", favourite_movies[0]['title'])

if favourite_movies[1]["is_published_after_2000"] != True:
    print("This movie is newer than 2000:", favourite_movies[1]['title'])
else:
    print("This movie is older than 2000:", favourite_movies[1]['title'])

# Compare the publishing year

if favourite_movies[0]["year"] <= 2000:  # Использование оператора сравнения
    print("This movie is older than 2000:", favourite_movies[0]["title"])
else:
    print("This movie is newer than 2000:", favourite_movies[0]["title"])

if favourite_movies[1]["year"] <= 2000:
    print("This movie is older than 2000:", favourite_movies[1]["title"])
else:
    print("This movie is newer than 2000:", favourite_movies[1]["title"])

# Combine the results using loops and conditionals

for movie in favourite_movies:
    if movie["year"] <= 2000:
        print("This movie is older than 2000:", movie["title"])
    else:
        print("This movie is newer than 2000:", movie["title"])