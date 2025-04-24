from pyswip import Prolog as plg

prolog = plg()

prolog.consult("hechos.pl")

pregunta = input('¿Que le gusta a...? ')

for valor in prolog.query("le_gusta(" + pregunta + ", Y)."):
    print(pregunta, "Le gusta ", valor['Y'])
