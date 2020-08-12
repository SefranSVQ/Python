# Funciones en Python
# 
# Sintaxis -> 
#   def nombre_funcion(parametros):
#       instrucciones
#   return \opcional
#
# Notas:
#   - Para tener una entrada indefinida de elementos, se le indica con un * antes del elemento a recibir, 
#   el cual tendrá los elementos introducidos en formato de tupla. Ejem: miFuncion(*tuplaElementos)
#
#
#


def holamundo():
    print ("Hola mundo cruel!")

def suma(num1,num2):
    result = num1+num2
    return result

def division(num1,num2):    # Uso de excepción para capturar problemas, como las divisiones entre 0
    try:
        result = num1/num2
    except:     # si se usa except solamente, capturará todas las opciones de errores, si usas except nombre_excepcion, lanzará el bloque solo cuando pase dicho error
        result = "error, introduzca valores válidos"
        # No es necesario el bloque finally en este caso.
    return result


def pokemonIniciales():
    pokemon={1:"Bulbasaur",2:"Charmander",3:"Squirtle",4:"Pikachu",5:"Eevee",6:"Clefairy"}
    return pokemon


# Esto es un "generador", un tipo especial de función que, en un conjunto de valores devueltos, nos los irán devolviendo de 1 en 1
# Es similar a una función estándar, solo que es en determinados casos es más eficiente usarla, ya que se almacena en memoria
# un único valor, en vez de una estructura de datos compleja.

""" 
generadorPokemon

Generador usado para devolver nombres de pokemon en orden de su número en la pokedex.
Entradas: 
    - Límite: entero, indica la cantidad de nombres de pokemon que deseas generar
Salidas / elementos generados:
    - pokemon: String, indica el nombre del pokemon generado
Precondiciones: el límite debe ser un valor comprendido entre el 1 y el 151

"""

def generadorPokemon(limite):
    contador=0
    listaPokemon=["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle",
	"Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀",
	"Nidorina","Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom",
	"Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag",
	"Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler",
	"Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch’d","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly",
	"Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung",
	"Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz",
	"Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl",
	"Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]

    while contador<=limite:

        pokemon = listaPokemon[limite]
        yield pokemon
        contador+=1

