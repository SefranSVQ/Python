# Clase especiePokemon

class especiePokemon():

    # Constructor

    def __init__(self,nombre,tipo1,tipo2,ataque,defensa,aguante):
        self.nombre=nombre
        self.tipo1=tipo1
        self.tipo2=tipo2
        self.ataque=ataque
        self.defensa=defensa
        self.aguante=aguante

    
    # Métodos

    def calcularCP(self,nivel,IVAtaque,IVDefensa,IVAguante):  
        multiplicadorCP=[0.094, 0.16639787, 0.21573247, 0.25572005, 0.29024988, 0.3210876, 	0.34921268, 0.3752356, 0.39956728, 0.4225,  #Habría que cambiar todos los strings para que fuesen exactos o bien recrear la fórmula incremental
                        0.443, 0.463, 0.482, 0.5, 0.517, 0.534, 0.551, 0.567, 0.582, 0.597, 
                        0.612, 0.627, 0.641, 0.654, 0.668, 0.681, 0.694, 0.707, 0.719, 0.732, 
                        0.738, 0.744, 0.75, 0.756, 0.762, 0.767, 0.773, 0.779, 0.785, 0.79]
        cp=0
        nivelValido=False

        nivelValido = self.__comprobarNivel(nivel)

        if not nivelValido:
            cp="error nivel" #cambiar por excepción
        else:
            cp=((self.ataque + IVAtaque) * pow(self.defensa + IVDefensa,0.5) * pow(self.aguante + IVAguante,0.5) * pow(multiplicadorCP[nivel-1],2)) / 10
            
        return cp

    

    def calcularHP(self,nivel):
        pass

    def mostrarEstado(self):
        print("Pokemon: ", self.nombre, "\nTipo 1: ", self.tipo1, "\nTipo 2: ", self.tipo2, "\nEstadísticas base: ", self.ataque,"-",self.defensa,"-",self.aguante,"\n")

    """
    comprobarNivel
    - Nos permite saber si el nivel introducido es válido o no
    - Entradas: nivel (decimal)
    - Salidas: nivelValido (bool)
    """

    def __comprobarNivel(self,nivel):
        nivelValido=False
        if 1.0<=nivel<=40.0:
            nivelValido=True
        return nivelValido
                

# Herencia

class megaEvolucion(especiePokemon):

    def __init__(self,forma,nombre,tipo1,tipo2,ataque,defensa,aguante):
        super().__init__(nombre,tipo1,tipo2,ataque,defensa,aguante)
        self.forma=forma #Mega / Primigenia

    def mostrarEstado(self):
        print("Pokemon: ", self.nombre,"\nForma: ", self.forma, "\nTipo 1: ", self.tipo1, "\nTipo 2: ", self.tipo2, 
        "\nEstadísticas base: ", self.ataque,"-",self.defensa,"-",self.aguante,"\n")


# Test
pokemon = especiePokemon("Pidgeot","normal","volador",166,154,195)
print(f"El CP de {pokemon.nombre} al nivel 8 con los IV 1,12,5 es de {str(int(pokemon.calcularCP(8,1,12,5)))}")
print("\n")

pokemon.mostrarEstado()

megaPokemon = megaEvolucion("Megaevolucion","Pidgeot","normal","volador",266,254,245)
megaPokemon.mostrarEstado()

megaPokemon = megaEvolucion("Primigenia","Groudon","Tierra","Fuego",300,300,300)
megaPokemon.mostrarEstado()