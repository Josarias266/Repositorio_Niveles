import os

class luchador:  #aquí se define la clase principal para los avatares
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

#Avatares JA
chabelo = luchador("Chabelo", 10, 1, False, False, False, False, False, True)
tecun = luchador("Tecún Uman", 10, 1, False, False, False, False, False, True)
#Avatares FQ
arjona = luchador("Ricardo Arjona", 10, 1, False, False, False, False, False, True)
gaby = luchador("Gaby Moreno", 10, 1, False, False, False, False, False, True)
mcgregor = luchador("Conor Mcgregor", 10, 1, False, False, False, False, False, True)
#Avatares JP
jake = luchador("Jake Paul", 10, 1, False, False, False, False, False, True)
siuu = luchador("El Bicho", 10, 1, False, False, False, False, False, True)
#Avatares RS
reina = luchador("La Reina Izabel", 10, 1, False, False, False, False, False, True)
jackie = luchador("Jackie Chan", 10, 1, False, False, False, False, False, True)
#Avatares KA
trump = luchador("Trump", 10, 1, False, False, False, False, False, True)
messi = luchador("Messi Chikito", 10, 1, False, False, False, False, False, True)

print ("Bienvenido!")
def players():      #Sección 1 --- Cantidad de jugadores
  try:
    amount = int(input("Cuantos jugadores habrán? "))
    if amount == 1:
        print("Solo habrá un jugador")
    elif amount == 2:
        print("Habrán dos jugadores")
    else:
        input ("Solo pueden haber 1 o 2 jugadores, presiona enter para volver a intentarlo...")
        os.system ("cls")
        players()
  except ValueError:
    input ("Solo puedes introducir valores numéricos, presiona enter para volver a intertarlo...")
    os.system ("cls")
    players()

def selection():    #Sección 2 --- Función para selección de personaje
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
    print ("Trump")
    print ("Messi Chikito")
    
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
    elif choose == "TRUMP":
        selectionated = trump
        choise()
    elif choose == "MESSI CHIKITO":
        selectionated = messi
        choise()
    else:
        os.system ("cls") # "cls" en windows y "clear" en mac/replit
        restart = "Intentalo de Nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      selection()
    except NameError:
      input ("Presiona la tecla enter para empezar el juego...")
      os.system ("cls")

def prints():       #Sección Pre-Final --- Estado de los avatares
    if chabelo.selected:
        print(chabelo.escogido())
    elif tecun.selected:
        print(tecun.escogido())
    elif arjona.selected:
        print(arjona.escogido())
    elif gaby.selected:
        print(gaby.escogido())
    elif mcgregor.selected:
        print(mcgregor.escogido())
    elif jake.selected:
        print(jake.escogido())
    elif reina.selected:
        print(reina.escogido())
    elif siuu.selected:
        print(siuu.escogido())
    elif jackie.selected:
        print(jackie.escogido())
    elif trump.selected:
        print(trump.escogido())
    else:
        print(messi.escogido())

def exports():      #Sección Final --- Exportar datos a Json
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
    export.write(trump.escogido() + "\n")
    export.write(messi.escogido() + "\n")
    export.close()

#Índice de Secciones del código
players()       #Sección 1 --- Cantidad de jugadores
selection()     #Sección 2 --- Función para selección de personaje
prints()        #Sección Pre-Final --- Estado de los avatares
exports()       #Sección Final --- Exportar datos a Json



input ("Presiona la tecla enter para salir...")
