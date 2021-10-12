import os

class luchador:  #aquí se define la clase principal para los obstáculos
    def __init__(self, name, hp, ap, patada, manada, defbaja, defalta, selected, alive):  #aquí se define el constructor
        self.name = name
        self.hp = hp
        self.ap = ap
        self.patada = patada
        self.manada = manada
        self.defbaja = defbaja
        self.defalta = defalta
        self.selected = selected    #Por defecto el luchador no está seleccionado
        self.alive = alive  #el estado por defecto del luchador es "vivo", "True"

    def matar(self):  #método para cambiar el estado del enemigo a "muerto", "False"
        self.alive = False

    def character(self):  #método para indicar el personaje seleccionado
        self.selected = True

    def estado(self):  #método para informar sobre el estado del enemigo
        if (self.alive):
            return "El enemigo " + (self.name) + " sigue con vida"
        else:
            return "El enemigo " + (self.name) + " ha muerto"
    
    def escogido(self):
        if (self.selected):
            return "El luchador " + (self.name) + " ha sido seleccionado"
        else:
            return "El luchador " + (self.name) + " no ha sido seleccionado"

chabelo = luchador("Chabelo", 10, 1, False, False, False, False, False, True)
tecun = luchador("Tecún Uman", 10, 1, False, False, False, False, False, True)
arjona = luchador("Ricardo Arjona", 10, 1, False, False, False, False, False, True)
gaby = luchador("Gaby Moreno", 10, 1, False, False, False, False, False, True)
mcgregor = luchador("Conor Mcgregor", 10, 1, False, False, False, False, False, True)
jake = luchador("Jake Paul", 10, 1, False, False, False, False, False, True)
reina = luchador("La Reina Izabel", 10, 1, False, False, False, False, False, True)
siuu = luchador("El Bicho", 10, 1, False, False, False, False, False, True)
jackie = luchador("Jackie Chan", 10, 1, False, False, False, False, False, True)
buitre1 = luchador("Jalks", 10, 1, False, False, False, False, False, True)
wolfman = luchador("Lucas", 10, 1, False, False, False, False, False, True)

print ("Bienvenido!")
def selection():    #Sección 1, selección de personaje
    print ("Escoje tu luchador!")
    print ("Chabelo")
    print ("Tecún Uman")
    print ("Ricardo Arjona")
    print ("Gaby Moreno")
    print ("Conor Mcgregor")
    print ("Jake Paul")
    print ("El Bicho")
    print ("Reina Isabel")
    print ("Jackie Chan")
    print ("Jalks")
    print ("Lucas")
    
    def choise():
        selectionated.character()

    choose = input("¿Qué avatar quieres utilizar?: ")
    choose = choose.upper()
    if choose == "CHABELO":
        selectionated = chabelo
        choise()
    elif choose == "TECUN UMAN":
        selectionated = tecun
        choise()
    elif choose == "RICARDO ARJONA":
        selectionated = arjona
        choise()
    elif choose == "GABY MORENO":
        selectionated = gaby
        choise()
    elif choose == "CONOR MCGREGOR":
        selectionated = mcgregor
        choise()
    elif choose == "JAKE PAUL":
        selectionated = jake
        choise()
    elif choose == "EL BICHO":
        selectionated = siuu
        choise()
    elif choose == "REINA ISABEL":
        selectionated = reina
        choise()
    elif choose == "JACKIE CHAN":
        selectionated = jackie
        choise()
    elif choose == "JALKS":
        selectionated = buitre1
        choise()
    elif choose == "LUCAS":
        selectionated = wolfman
        choise()
    else:
        os.system ("cls") # "cls" en windows y "clear" en mac/replit
        restart = "Intentalo de Nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      selection()
    except NameError:
      input ("Presiona la tecla enter para ver los resultados...")
      os.system ("cls")

selection()

#Estado final de los enemigos
print(chabelo.escogido())
print(tecun.escogido())
print(arjona.escogido())
print(gaby.escogido())
print(mcgregor.escogido())
print(jake.escogido())
print(reina.escogido())
print(siuu.escogido())
print(jackie.escogido())
print(buitre1.escogido())
print(wolfman.escogido())

input ("Presiona la tecla enter para salir...")


#Exportar datos a Json
export = open("Resultados_Nivel.json", "w")
export.write("Estos son los resultados del nivel: \n")
export.write(chabelo.escogido() + "\n")
export.write(tecun.escogido() + "\n")
export.write(arjona.escogido() + "\n")
export.write(gaby.escogido() + "\n")
export.write(mcgregor.escogido() + "\n")
export.write(jake.escogido() + "\n")
export.write(siuu.escogido() + "\n")
export.write(reina.escogido() + "\n")
export.write(jackie.escogido() + "\n")
export.write(buitre1.escogido() + "\n")
export.write(wolfman.escogido() + "\n")
export.close()

#Pendiente evaluar si el nivel es superado al vencer luchadores
#Pendiente funcion para disminuir la resistencia
#Pendiente funcion de nueva habilidad jugador
#Pendiente nueva habilidad luchador