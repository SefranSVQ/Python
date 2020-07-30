# Mini pruebas con Operadores

iniciales=["Charmander","Squirtle","Bulbasaur"] 

pkmn=input("Escribe tu pkmn inicial: Bulbasaur - Charmander - Squirtle: ")
pkmn=pkmn.lower() # Lo pone todo en minusculas, no es necesario para el ejemplo, pero bueh. Contraparte de upper()
pkmn=pkmn.capitalize() # Pone el string como si fuese un nombre propio; primera letra en mayusc

if pkmn in (iniciales):
    print("todo ok, toma tu "+pkmn)
else:
    print("escoge bien")

if pkmn == iniciales[0] or pkmn == iniciales[2]:
    print("tienes buen gusto")
