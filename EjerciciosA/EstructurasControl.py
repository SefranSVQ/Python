# (Las clásicas) Estructuras de control de flujo

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

# Switch
# Jaja saludos - No existen.

