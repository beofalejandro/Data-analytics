from pyswip import Prolog as plg

prolog = plg()
prolog.consult("hechos.pl")

pregunta = input('¿Que le gusta a...? ')

for valor in prolog.query("Le gusta (" + pregunta + ")."):
    print(pregunta, "Le gusta a", valor['X'])