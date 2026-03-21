
def create_movie_database(titles, years, genres, ratings):

    print("Checking if all lists have same length.")

    if len(titles) != len(years) or len(titles) != len(genres) or len(titles) != len(ratings):
        print("Lists are not the same length!")
        return []

    movie_list = []

    for i in range(len(titles)):

        if ratings[i] < 0 or ratings[i] > 10:
            print("Invalid rating for:", titles[i])
            continue

        movie = {
            "title": titles[i],
            "year": years[i],
            "genre": genres[i],
            "rating": ratings[i]
        }

        movie_list.append(movie)

    print("Database created successfully!\n")
    return movie_list


def filter_by_genre(movies, genre):
    result = list(filter(lambda movie: movie["genre"].lower() == genre.lower(), movies))
    return result


def filter_by_rating(movies, min_rating):
    result = list(filter(lambda item: item["rating"] >= min_rating, movies))
    return result


def sort_movies(movies, by="rating"):

    if by == "rating":
        sorted_list = sorted(movies, key=lambda a: a["rating"], reverse=True)
    elif by == "year":
        sorted_list = sorted(movies, key=lambda b: b["year"])
    elif by == "title":
        sorted_list = sorted(movies, key=lambda c: c["title"])
    else:
        print("invalid sorting option. sorting by rating.")
        sorted_list = sorted(movies, key=lambda d: d["rating"], reverse=True)

    return sorted_list


def top_n_movies(movies, n=5):
    sorted_list = sort_movies(movies, "rating")
    return sorted_list[:n]

def display_ranked_list(movies):

    if len(movies) == 0:
        print("No movies to show.")
        return

    for i, movie in enumerate(movies, start=1):
        print(str(i) + ". " + movie["title"] + 
              " (" + str(movie["year"]) + ")" +
              " - " + movie["genre"] +
              " - " + str(movie["rating"]) + "/10")
    print()


def calculate_average_rating(movies):

    if len(movies) == 0:
        return 0

    total = 0
    for movie in movies:
        total = total + movie["rating"]

    average = total / len(movies)
    return round(average, 2)


def find_by_year(movies, year):
    result = []
    for movie in movies:
        if movie["year"] == year:
            result.append(movie)
    return result


print("===== MOVIE RECOMMENDATION SYSTEM =====")

titles = ["dark night",
          "umbrella",
          "hello mom",
          "alive",
          "lufa",
          "king"]

years = [2006, 2000, 2012, 2015, 2020, 1968]

genres = ["comedy", "comedy", "action", "historical", "historical", "comedy"]

ratings = [9.0, 9.3, 8.8, 7.2, 7.7, 8.8]

movies = create_movie_database(titles, years, genres, ratings)

print("===== ALL MOVIES =====")
display_ranked_list(movies)

print("===== FILTER: comedy =====")
sci_fi = filter_by_genre(movies, "comedy")
display_ranked_list(sci_fi)

print("===== FILTER: Rating >= 8.8 =====")
high_rating = filter_by_rating(movies, 8.8)
display_ranked_list(high_rating)

print("===== TOP 3 MOVIES (by rating)=====")
top3 = top_n_movies(movies, 3)
display_ranked_list(top3)

print("===== SORTED BY YEAR =====")
sorted_by_year = sort_movies(movies, "year")
display_ranked_list(sorted_by_year)


print("===== STATISTICS =====")
print("Total movies:", len(movies))
print("Average rating:", calculate_average_rating(movies), "/10")

