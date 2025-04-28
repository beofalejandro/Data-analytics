import recomender as rc

mood_options = {
    '1': 'feliz',
    '2': 'triste',
    '3': 'acción',
    '4': 'enojado',
    '5': 'sorprendido'
}

while True:
    decision = input("¿Quieres ver recomendaciones de películas?\n[1]: Sí \n[2]: No, Salir ")
    if decision == '1':
        print("Bienvenido al sistema de recomendación de películas.")
        print("Selecciona tu estado de ánimo:")
        print("[1] Feliz")
        print("[2] Triste")
        print("[3] Acción")
        print("[4] Enojado")
        print("[5] Sorprendido")
        
        mood_number = input("Ingresa el número correspondiente a tu estado de ánimo: ").strip()
        mood = mood_options.get(mood_number)

        if mood is None:
            print("Opción no válida. Intenta de nuevo.")
            continue
        
        age = int(input("¿Qué edad tienes?: "))

        recommended = rc.recommend_movies(mood=mood, age=age)

        print("\nTal vez deberías ver:\n")
        if recommended:
            for name, year, rating, genres in recommended:
                print(f"{name} ({year}) - Rating: {rating} - Genres: {', '.join(genres)}")
            print("\n")
        else:
            print("No se encontraron recomendaciones para tus criterios.")
    elif decision == '2':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")