# (Las clásicas) Estructuras de control de flujo
import Funciones
import math

"""
# if, elif, else
nota=float(input("Pon tu nota (solo valores numéricos): "))
calificacion=""

if 0<=nota<5:       #Concatenación de operadores de comparación
    calificacion="suspenso"
elif nota<6:
    calificacion="aprobado"
elif nota<7:
    calificacion="bien"
elif nota<9:
    calificacion="notable"
elif nota<=10:
    calificacion="sobresaliente"
else:
    calificacion="error"

print(calificacion)
"""

# Switch
# Jaja saludos - No existen.
# hay que usar tipos de datos como los diccionarios para simular esta estructura de control

"""
Futuro ejemplo
"""


"""
# Bucle for
for i in range(10):
    print(str(i+1))

for i in range(5,10):
    print(str(i+1))

# Usando un diccionario, i tomará el valor de la clave
pokemon=Funciones.pokemonIniciales()

for i in pokemon:
    print (f"Pokemon Inicial Nº {i}: "+pokemon.get(i))

# Usando un string, se recorrerá el bucle en función de la cantidad de caracteres que este contenga, tomando i el valor del caracter que corresponda.
for i in "hola":
    print (str(i))

# Si se usan varios strings (o cualquier otro elemento), se tomará como una lista, tomando i el valor de cada elemento en dicha lista
for i in "hola","Adios":
    print (str(i))

"""

"""
#Bucles while

iterar = True

while iterar:
    numero=input("Escribe un número entero de entre 0 a 10 -> ")
    if not(0<=int(numero)<=10):
        print("Incorrecto, vuelve a intentarlo.")
    else:
        iterar=False
        
print("Correcto!")
"""

"""
# Llamada al generadorPokemon()

for i in range(151):
    print(next(Funciones.generadorPokemon(i)))
    print("Espacio en memoria: "+str(Funciones.generadorPokemon(i))) #Aqui podemos observar como siempre usa el mismo espacio en memoria
"""


# Llamada a la funcion "Division", la cual contiene un bloque try-except

result = Funciones.division(2,0)

print(str(result))
