from pyswip import Prolog

prolog = Prolog()
prolog.consult("movies.pl")

def recommend_movies(mood=None, age=None):
    recommendations = []

    for movie in prolog.query("movie(Name, Year, Rating, Genre, RunTime)"):
        name = movie['Name']
        year = movie['Year']
        rating = movie['Rating']
        genre_list = movie['Genre'].split(',')

        is_action = 'Action' in genre_list
        is_fantasy = 'Fantasy' in genre_list
        is_adventure = 'Adventure' in genre_list
        is_animation = 'Animation' in genre_list
        is_drama = 'Drama' in genre_list
        is_comedy = 'Comedy' in genre_list
        is_thriller = 'Thriller' in genre_list
        is_romance = 'Romance' in genre_list
        is_family = 'Family' in genre_list
        is_high_rating = rating >= 8.0

        if mood == 'feliz':
            if age <= 12 and (is_animation or is_family):
                recommendations.append((name, year, rating, genre_list))
            elif age > 12 and (is_comedy or is_adventure):
                recommendations.append((name, year, rating, genre_list))
        elif mood == 'triste' and (is_drama or is_romance):
            recommendations.append((name, year, rating, genre_list))
        elif mood == 'acción' and is_action:
            recommendations.append((name, year, rating, genre_list))
        elif mood == 'enojado' and (is_action or is_thriller):
            recommendations.append((name, year, rating, genre_list))
        elif mood == 'sorprendido' and (is_fantasy or 'Mystery' in genre_list):
            recommendations.append((name, year, rating, genre_list))

        if len(recommendations) >= 7:
            break

    return recommendations