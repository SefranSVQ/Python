# Introducción a Python
#
# Creador @SefranSVQ
#
# Calidad, buenas prácticas, recomendaciones e información general del lenguaje:
#
# - 1 línea -> 1 instrucción. 
# - Puedes usar ; para poner varias instrucciones, pero no es recomendable.
# - No se usa ; al final de cada línea si no es con la intención anterior.
# - Lenguaje no tipado 
# - 100% orientado a objetos -> todo es un objeto
# - Siempre se pasan los valores por referencia
# - 

# Inicio

#Ficheros importados

#from Funciones import * # Para importarlo todo sin necesidad de llamar al fichero

from Funciones import suma,holamundo

# Función print() -> imprimir por pantalla
print("Hola mundo") 

# Tipos de datos más usados: int, float, str, bool
entero = 6
decimal = 1.2
cadena = "ejemplo"
booleano = True

# Operadores:
# - Aritméticos: +, -, *, /, %, **, //...
# - Concatenación + -> sólo cadenas y listas.
# - Comparación: ==, >=, >, <, <=, !=
# - Asignación: =, +=, -=,...
# - Lógicos y Especiales: AND, OR, NOT, IS, IS NOT, IN, NOT IN...

# Para concatenar distintos tipos de datos en una cadena, debemos castear al tipo de dato string con la función str() en cada uno de los valores a introducir en dicha cadena.
print ("Ejemplos de tipos de datos: "+str(entero)+" - "+str(decimal)+" - "+cadena+" - "+str(booleano))

# Función type() -> nos permite saber el tipo de dato almacenado en una variable.
print ("Y aquí sus tipos correspondientes:")
print (type(entero))
print (type(decimal))
print (type(cadena))
print (type(booleano))

#Llamadas a funciones alojadas en el fichero "funciones"
print("Llamadas a funciones:")
holamundo()

resultado = suma(1,4)
print (str(resultado))

# Listas
#   Notas: 
#   - Permiten almacenar diferentes tipos de valores.
#   - Si introduces un índice negativo, empieza desde el final de la lista -> [-2] -> segundo valor empezando desde el final.
#   - Permite poner un rango de valores, el primer número será inclusivo y el último exclusivo. -> [1:4] -> muestra los valores de entre la segunda a la cuarta posicion
#   - Si omites el primer número en el rango, entenderá que es desde el inicio. -> [:4]
#   - Si omites el segundo número en el rango, entenderá que es hasta el final. -> [0:]
#   - Si omites el ambos números en el rango, entenderá que es a la lista entera -> [:]
# Sintaxis: lista=[elemento1,elemento2,...] 

print("Probamos las listas:")
pokemon=["Bulbasaur","Charmander","Squirtle","Pikachu"]

print("Escoge a uno: "+str(pokemon[:4]))

print("¿Seguro que quieres escoger a "+pokemon[1]+"?")

pokemon.append("Weedle") # Introduce el elemento al final. Nota: para introducir varios elementos, usar extend, sino anidará los elementos como una nueva lista en ese espacio.
pokemon.insert(4,"Caterpie") # Introduce el elemento tras el elemento indicado
pokemon.extend(["Pidgey","Rattata"]) # Introduce varios elementos a la lista.
pokemon.index("Pikachu") # Devuelve la posición del elemento introducido.
"Sandrew" in pokemon # Devuelve un valor booleano en función de si se encuentra o no el elemento en la lista.
pokemon.remove("Pikachu") # Elimina el elemento introducido. Tambien puedes introducir el índice.
pokemon.pop() # Elimina el último elemento de la lista.
pokemon=pokemon*2 # Se pueden añadir una cantidad definida de veces los elementos a una lista.

print(len(pokemon)) # Para saber la longitud de una lista hay que usar la función Len(), no existe un método.

print(pokemon)


# Tuplas
#   - Son listas inmutables -> no se pueden modificar tras su creación.
#   - Permiten comprobar si un elemento existe dentro de ella.
#   - Sus ventajas principales son: más rápida, menor espacio en memoria, formatean strings y pueden usarse como claves de un diccionario.
# Sintaxis: tupla=(elemento1,elemento2,...) -> Se pueden omitir los paréntesis, aunque es recomendable usarlos.

tupla=("Sefran",2,9,1992)

# Desempaquetado de tupla
nombre,día,mes,anyo=tupla

print(tupla)
print(nombre)
print(día)
print(mes)
print(anyo)

# Diccionarios
#   - Estructura de datos similar a las anteriores. 
#   - Su principal característica principal es la asociación de claves a cada uno de sus valores.
#   - como en el resto de las estructuras anteriores, se pueden incluir distintos tipos y estructuras de datos dentro de ella
# Sintaxis: diccionario={clave1:elem1,clave2:elem2,...}

diccionario = {1:"Bulbasaur",2:"Ivysaur",3:"Venusaur"}

print(diccionario)
print(diccionario.get(2))

# Introducción de un elemento
diccionario[4]="Squirtle"

print(diccionario)

# Modificación de un elemento
diccionario[4]="Charmander"

print(diccionario)

# Solo las claves
print(diccionario.keys())

# Solo los valores
print(diccionario.values())