import recomender as rc  # Recomender class
import recomenderhappinestess as rch  # RecomenderHappiness class

while True:

    print(
        "Bienvenido al sistema de recomendaciones de películas. \n [1]: Pedir recomendación a base de una pelicula vista \n [2]: Recomendacion de acuerdo a tu estado de animo \n [3]: Salir")

    decision = input("¿Qué deseas hacer? (1/2/3): ")

    if decision == '1':
        pelicula_vista = input("Introduce la película que has visto: ")
        recomendaciones = rc.recomendar(str(pelicula_vista))

        if isinstance(recomendaciones, list) and recomendaciones:
            print(f'Por que viste "{pelicula_vista}": \nDeberias ver:')
            for recomendacion in recomendaciones:
                print(f'- {recomendacion}')
            print("\n")
        else:
            print("No hay recomendaciones disponibles.")
            print("\n")

    if decision == '2':
            estado_animo = input("Introduce tu estado de ánimo (feliz, triste, temeroso, emocionado, pensativo): ").strip().lower()
            recomendaciones = rch.recomendar_peliculas_por_animo(estado_animo)
            if isinstance(recomendaciones, list) and recomendaciones:
                print(f'Recomendaciones para el estado de ánimo "{estado_animo}":')
                for pelicula in recomendaciones:
                    print(f'- {pelicula}')
                print("\n")
            else:
                print(recomendaciones)
                print("\n")

    elif decision == '3':
        print("Gracias por usar el sistema de recomendaciones. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        print("\n")
