import src.family_founder as child

while True:
        print("Bienvenido al sistema de búsqueda familiar. \n [1]: Buscar padres de un niño \n [2]: Buscar Hijos de un padre \n [3]: Buscar Hermanos \n [4]: Buscar Primos \n [5]: Salir")
    
        decision = input("¿Qué deseas hacer? (1/2): ")
    
        if decision == '1':
            nombre_usuario = input("Introduce el nombre: ").strip()
            
            padres = child.encontrar_padres(nombre_usuario)
            
            if padres:
                print(f"Los padres de {nombre_usuario} son: {', '.join(padres)}.")
            else:
                print(f"No se encontraron padres de {nombre_usuario}.")
            print("\n")
        elif decision == '2':
            nombre_usuario = input("Introduce el nombre: ").strip()
            
            hijos = child.encontrar_hijos(nombre_usuario)
            
            if hijos:
                print(f"Los hijos de {nombre_usuario} son: {', '.join(hijos)}.")
            else:
                print(f"No se encontraron hijos de {nombre_usuario}.")
            print("\n")

        elif decision == '3':
            nombre_usuario = input("Introduce el nombre: ").strip()
            
            hermanos = child.encontrar_hermanos(nombre_usuario)
            
            if hermanos:
                print(f"Los hermanos de {nombre_usuario} son: {', '.join(hermanos)}.")
            else:
                print(f"No se encontraron hermanos de {nombre_usuario}.")
            print("\n")
        
        elif decision == '4':
            nombre_usuario = input("Introduce el nombre: ").strip()
            
            primos = child.encontrar_primos(nombre_usuario)
            
            if primos:
                print(f"Los primos de {nombre_usuario} son: {', '.join(primos)}.")
            else:
                print(f"No se encontraron primos de {nombre_usuario}.")
            print("\n")
    
        elif decision == '5':
            print("Gracias por usar el sistema de búsqueda de padres. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
            print("\n")
