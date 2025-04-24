import recomender as rc # System of recommendation

while True:
    # Get the movie name from the user
    pelicula_vista = input("Introduce la pelicula que has visto: ")
    rc.recomendar(pelicula_vista)
