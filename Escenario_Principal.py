import os

class obstaculo:  #aquí se define la clase principal para los obstáculos
    def __init__(self, name, hp, ap, patada, manada, defbaja, defalta, selected, alive):  #aquí se define el constructor
        self.name = name
        self.hp = hp
        self.ap = ap
        self.patada = patada
        self.manada = manada
        self.defbaja = defbaja
        self.defalta = defalta
        self.selected = selected
        self.alive = alive  #el estado por defecto del enemigo es "vivo", "True"

    def matar(self):  #método para cambiar el estado del enemigo a "muerto", "False"
        self.alive = False

    def character(self):  #método para indicar el personaje seleccionado
        self.selected = True

    def estado(self):  #método para informar sobre el estado del enemigo
        if (self.alive):
            return "El enemigo " + (self.name) + " sigue con vida"
        else:
            return "El enemigo " + (self.name) + " ha muerto"

chabelo = obstaculo("Chabelo", 10, 1, False, False, False, False, False, True)
tecun = obstaculo("Tecún Uman", 10, 1, False, False, False, False, False, True)
arjona = obstaculo("Ricardo Arjona", 10, 1, False, False, False, False, False, True)
gaby = obstaculo("Gaby Moreno", 10, 1, False, False, False, False, False, True)
mcgregor = obstaculo("Conor Mcgregor", 10, 1, False, False, False, False, False, True)
jake = obstaculo("Jake Paul", 10, 1, False, False, False, False, False, True)
reina = obstaculo("La Reina Izabel", 10, 1, False, False, False, False, False, True)
siuu = obstaculo("El Bicho", 10, 1, False, False, False, False, False, True)
jackie = obstaculo("Jackie Chan", 10, 1, False, False, False, False, False, True)
buitre1 = obstaculo("Jalks", 10, 1, False, False, False, False, False, True)
wolfman = obstaculo("Lucas", 10, 1, False, False, False, False, False, True)

print ("Bienvenido!")
def selection():
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

    choose = input("¿Qué enemigo quieres derrotar?: ")
    choose = choose.upper()
    if choose == "CHABELO":
        selectionated = chabelo
        choise()
    elif choose == "TECUN UMAN" or "TECÚN UMAN":
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
print(chabelo.estado())
print(tecun.estado())
print(arjona.estado())
print(gaby.estado())
print(mcgregor.estado())
print(jake.estado())
print(reina.estado())
print(siuu.estado())
print(jackie.estado())
print(buitre1.estado())
print(wolfman.estado())

input ("Presiona la tecla enter para salir...")


#Exportar datos a Json
export = open("Resultados_Nivel.json", "w")
export.write("Estos son los resultados del nivel: \n")
export.write(chabelo.estado() + "\n")
export.write(tecun.estado() + "\n")
export.write(arjona.estado() + "\n")
export.write(gaby.estado() + "\n")
export.write(mcgregor.estado() + "\n")
export.write(jake.estado() + "\n")
export.write(siuu.estado() + "\n")
export.write(reina.estado() + "\n")
export.write(jackie.estado() + "\n")
export.write(buitre1.estado() + "\n")
export.write(wolfman.estado() + "\n")
export.close()

#Pendiente evaluar si el nivel es superado al vencer obstaculos
#Pendiente funcion para disminuir la resistencia
#Pendiente funcion de nueva habilidad jugador
#Pendiente nueva habilidad obstaculo