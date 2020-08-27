# Manejo de ficheros básico

from io import open

# Creación/apertura de un archivo e introducción de una frase

archivo_txt=open("archivo.txt","w")

frase="Probando la introducción de una cadena en un fichero."
archivo_txt.write(frase)

archivo_txt.close()

# Lectura
archivo_txt=open("archivo.txt","r")
frase="Probando la introducción de una cadena en un fichero. \n"

print("Lectura simple del fichero")
frase+=archivo_txt.read()
print(frase)
archivo_txt.close()

# Escritura y lectura en formato lista
archivo_txt=open("archivo.txt","w")
print("Introducción de 2 líneas al fichero")
archivo_txt.write(frase)
archivo_txt.close()

archivo_txt=open("archivo.txt","r")
frase=archivo_txt.readlines()
print("Lectura e impresión del fichero en formato lista")
print(frase)
archivo_txt.close()

# Agregar nuevas entradas al fichero
print("Introducción de una tercera línea al fichero")
archivo_txt=open("archivo.txt","a")
archivo_txt.write("\ntercera línea del archivo")
archivo_txt.close()

# Lectura por partes del fichero.
print("Lectura del fichero de 10 en 10 caracteres")
archivo_txt=open("archivo.txt","r")
sumatorio=0
totalCaracteres=len(archivo_txt.read())
archivo_txt.seek(0) #Posiciona el puntero al inicio del fichero
while sumatorio < totalCaracteres+10:
    print(archivo_txt.read(9))
    sumatorio+=10
archivo_txt.close()

# Manipulacion completa del fichero con e/s
print("Manipulacion completa del archivo")
archivo_txt=open("archivo.txt","r+")
archivo_txt.read()
archivo_txt.write("\nEsto es otra línea")
archivo_txt.seek(0)
print(archivo_txt.read())
archivo_txt.close()


