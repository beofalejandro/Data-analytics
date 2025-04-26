from pyswip import Prolog

prolog = Prolog()

prolog.consult("family.pl")

def encontrar_padres(nombre):
    resultado = list(prolog.query(f'es_hijo_de({nombre}, Padre)'))
    if resultado:
        padres = [r['Padre'] for r in resultado]
        return padres
    else:
        return None
    
def encontrar_hijos(nombre):
    resultado = list(prolog.query(f'es_padre_de({nombre}, Hijo)'))
    if resultado:
        hijos = [r['Hijo'] for r in resultado]
        return list(set(hijos))
    else:
        return None
    
def encontrar_hermanos(nombre):
    resultado = list(prolog.query(f'hermano_de({nombre}, Hermano)'))
    if resultado:
        hermanos = [r['Hermano'] for r in resultado]
        return list(set(hermanos))
    else:
        return None

def encontrar_primos(nombre):
    resultado = list(prolog.query(f'primo_de({nombre}, Primo)'))
    if resultado:
        primos = [r['Primo'] for r in resultado]
        return list(set(primos))
    else:
        return None