import os
import random

class luchador:  #aquí se define la clase principal para los avatares
    def __init__(self, name, hp, ap, patada, manada, defbaja, defalta, selected_1, selected_2, alive):  #aquí se define el constructor
        self.name = name
        self.hp = hp
        self.ap = ap
        self.patada = patada
        self.manada = manada
        self.defbaja = defbaja
        self.defalta = defalta
        self.selected_1 = selected_1
        self.selected_2 = selected_2
        self.alive = alive  #el estado por defecto del luchador es "vivo", "True"

    def matar(self):  #método para cambiar el estado del enemigo a "muerto", "False"
        self.alive = False

    def character_1(self):  #método para indicar el personaje seleccionado
        self.selected_1 = True
    
    def character_2(self):  #método para indicar el personaje seleccionado
        self.selected_2 = True

    def estado(self):  #método para informar sobre el estado del enemigo
        if (self.alive):
            return "El enemigo " + (self.name) + " sigue con vida"
        else:
            return "El enemigo " + (self.name) + " ha muerto"
    
    def escogido_1(self):
        if (self.selected_1):
            return (self.name)
        else:
            pass
    
    def escogido_2(self):
        if (self.selected_2):
            return (self.name)
        else:
            pass

#Avatares JA
chabelo = luchador("Chabelo", 10, 1, False, False, False, False, False, False, True)
tecun = luchador("Tecún Uman", 10, 1, False, False, False, False, False, False, True)
#Avatares FQ
arjona = luchador("Ricardo Arjona", 10, 1, False, False, False, False, False, False, True)
gaby = luchador("Gaby Moreno", 10, 1, False, False, False, False, False, False, True)
mcgregor = luchador("Conor Mcgregor", 10, 1, False, False, False, False, False, False, True)
#Avatares JP
jake = luchador("Jake Paul", 10, 1, False, False, False, False, False, False, True)
siuu = luchador("El Bicho", 10, 1, False, False, False, False, False, False, True)
#Avatares RS
reina = luchador("La Reina Isabel", 10, 1, False, False, False, False, False, False, True)
jackie = luchador("Jackie Chan", 10, 1, False, False, False, False, False, False, True)
#Avatares KA
trump = luchador("Trump", 10, 1, False, False, False, False, False, False, True)
messi = luchador("Messi Chikito", 10, 1, False, False, False, False, False, False, True)



def players():      #Sección 1 --- Cantidad de jugadores
    try:
        amount = int(input("Cuantos jugadores habrán? "))
        if amount == 1:
            os.system ("cls")
            player1_choose()
            bot_choose()
            index_1()
        elif amount == 2:
            os.system ("cls")
            player1_choose()
            player2_choose()
            index_2()
        else:
            input ("Solo pueden haber 1 o 2 jugadores, presiona enter para volver a intentarlo...")
            os.system ("cls")
            players()
    except ValueError:
        input ("Solo puedes introducir valores numéricos, presiona enter para volver a intertarlo...")
        os.system ("cls")
        players()

def index_1(): #Índice en caso de que solo haya un jugador
    prints_1()
    prints_2()
    input ("Presiona la tecla enter para iniciar el juego...")
    os.system("cls")
    print ("Turno del Jugador 1!")
    player_1_atack()
    player_1_defense()

def index_2(): #Índice en caso de que hayan dos jugadores
    prints_1()
    prints_2()
    input ("Presiona la tecla enter para iniciar el juego...")
    os.system("cls")
    print ("Turno del Jugador 1!")
    player_1_atack()
    player_1_defense()
    print ("Turno del Jugador 2!")
    player_2_atack()
    player_2_defense()

def selection_1():    #Sección 2.1 --- Función para selección de personaje
    print ("Escoje un personaje de la lista!")
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
        fighter_1.character_1()

    choose = input("¿Qué luchador quieres utilizar?: ")
    choose = choose.upper()
    if choose == "CHABELO":
        fighter_1 = chabelo
        choise()
    elif choose == "TECUN UMAN":
        fighter_1 = tecun
        choise()
    elif choose == "RICARDO ARJONA":
        fighter_1 = arjona
        choise()
    elif choose == "GABY MORENO":
        fighter_1 = gaby
        choise()
    elif choose == "CONOR MCGREGOR":
        fighter_1 = mcgregor
        choise()
    elif choose == "JAKE PAUL":
        fighter_1 = jake
        choise()
    elif choose == "EL BICHO":
        fighter_1 = siuu
        choise()
    elif choose == "REINA ISABEL":
        fighter_1 = reina
        choise()
    elif choose == "JACKIE CHAN":
        fighter_1 = jackie
        choise()
    elif choose == "TRUMP":
        fighter_1 = trump
        choise()
    elif choose == "MESSI CHIKITO":
        fighter_1 = messi
        choise()
    else:
        os.system ("cls") # "cls" en windows y "clear" en mac/replit
        restart = "Intentalo de Nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      selection_1()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

def selection_2():    #Sección 2.2 --- Función para selección de personaje
    print ("Escoje un personaje de la lista!")
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
        fighter_2.character_2()

    choose = input("¿Qué luchador quieres utilizar?: ")
    choose = choose.upper()
    if choose == "CHABELO":
        fighter_2 = chabelo
        choise()
    elif choose == "TECUN UMAN":
        fighter_2 = tecun
        choise()
    elif choose == "RICARDO ARJONA":
        fighter_2 = arjona
        choise()
    elif choose == "GABY MORENO":
        fighter_2 = gaby
        choise()
    elif choose == "CONOR MCGREGOR":
        fighter_2 = mcgregor
        choise()
    elif choose == "JAKE PAUL":
        fighter_2 = jake
        choise()
    elif choose == "EL BICHO":
        fighter_2 = siuu
        choise()
    elif choose == "REINA ISABEL":
        fighter_2 = reina
        choise()
    elif choose == "JACKIE CHAN":
        fighter_2 = jackie
        choise()
    elif choose == "TRUMP":
        fighter_2 = trump
        choise()
    elif choose == "MESSI CHIKITO":
        fighter_2 = messi
        choise()
    else:
        os.system ("cls") # "cls" en windows y "clear" en mac/replit
        restart = "Intentalo de Nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      selection_2()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

def player1_choose():
    print("Jugador 1 prepárate para escoger a tu luchador!")
    selection_1()

def player2_choose():
    print("Jugador 2 prepárate para escoger a tu luchador!")
    selection_2()

def bot_choose():

    def choice():
        fighter_2.character_2()

    choose = random.randint(1,11)
    if choose == 1:
        fighter_2 = chabelo
        choice()
    elif choose == 2:
        fighter_2 = tecun
        choice()
    elif choose == 3:
        fighter_2 = arjona
        choice()
    elif choose == 4:
        fighter_2 = gaby
        choice()
    elif choose == 5:
        fighter_2 = mcgregor
        choice()
    elif choose == 6:
        fighter_2 = jake
        choice()
    elif choose == 7:
        fighter_2 = siuu
        choice()
    elif choose == 8:
        fighter_2 = reina
        choice()
    elif choose == 9:
        fighter_2 = jackie
        choice()
    elif choose == 10:
        fighter_2 = trump
        choice()
    elif choose == 11:
        fighter_2 = messi
        choice()

def prints_1():       #Sección Pre-Final --- Estado de los avatares 1
    if chabelo.selected_1:
        print("El jugador 1 escogió a " + chabelo.escogido_1())
    elif tecun.selected_1:
        print("El jugador 1 escogió a " + tecun.escogido_1())
    elif arjona.selected_1:
        print("El jugador 1 escogió a " + arjona.escogido_1())
    elif gaby.selected_1:
        print("El jugador 1 escogió a " + gaby.escogido_1())
    elif mcgregor.selected_1:
        print("El jugador 1 escogió a " + mcgregor.escogido_1())
    elif jake.selected_1:
        print("El jugador 1 escogió a " + jake.escogido_1())
    elif reina.selected_1:
        print("El jugador 1 escogió a " + reina.escogido_1())
    elif siuu.selected_1:
        print("El jugador 1 escogió a " + siuu.escogido_1())
    elif jackie.selected_1:
        print("El jugador 1 escogió a " + jackie.escogido_1())
    elif trump.selected_1:
        print("El jugador 1 escogió a " + trump.escogido_1())
    elif messi.selected_1:
        print("El jugador 1 escogió a " + messi.escogido_1())
    else:
        pass

def prints_2():       #Sección Pre-Final --- Estado de los avatares 2
    if chabelo.selected_2:
        print("El jugador 2 escogió a " + chabelo.escogido_2())
    elif tecun.selected_2:
        print("El jugador 2 escogió a " + tecun.escogido_2())
    elif arjona.selected_2:
        print("El jugador 2 escogió a " + arjona.escogido_2())
    elif gaby.selected_2:
        print("El jugador 2 escogió a " + gaby.escogido_2())
    elif mcgregor.selected_2:
        print("El jugador 2 escogió a " + mcgregor.escogido_2())
    elif jake.selected_2:
        print("El jugador 2 escogió a " + jake.escogido_2())
    elif reina.selected_2:
        print("El jugador 2 escogió a " + reina.escogido_2())
    elif siuu.selected_2:
        print("El jugador 2 escogió a " + siuu.escogido_2())
    elif jackie.selected_2:
        print("El jugador 2 escogió a " + jackie.escogido_2())
    elif trump.selected_2:
        print("El jugador 2 escogió a " + trump.escogido_2())
    elif messi.selected_2:
        print("El jugador 2 escogió a " + messi.escogido_2())
    else:
        pass

def player_1_atack(): #Ataque del jugador 1

    def choise():
        golpe_1 = punch_1

    punch = input("Quieres tirar una patada o una manada?: ")
    punch = punch.upper()
    if punch == "PATADA":
        print("El jugador 1 tiró una patada")
        punch_1 = "manada"
        choise()
    elif punch == "MANADA":
        print("El jugador 1 tiró una manada")
        punch_1 = "patada"
        choise()
    else:
        os.system("cls")
        restart = "Vuelve a Intentarlo! Solo puedes dar una 'patada' o una 'manada'"
    try:
      print(restart)
      player_1_atack()
    except NameError:
      pass

def player_1_defense():
    defense = input("Quieres cubrirte la cara o las patas?: ")
    defense = defense.upper()
    if defense == "CARA":
        print("El jugador 1 se cubrió la cara")
        defense_1 = "def_alta"
    elif defense == "PATAS":
        print("El jugador 1 se cubrió las patas")
        defense_1 = "def_baja"
    else:
        os.system("cls")
        restart = "Vuelve a Intentarlo! Solo puedes cubrirte la 'cara' o las 'patas'"
    try:
      print(restart)
      player_1_defense()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

def player_2_atack(): #Ataque del jugador 2
    punch = input("Quieres tirar una patada o una manada?: ")
    punch = punch.upper()
    if punch == "PATADA":
        print("El jugador 2 tiró una patada")
        punch_2 = "manada"
    elif punch == "MANADA":
        print("El jugador 2 tiró una manada")
        punch_2 = "patada"
    else:
        os.system("cls")
        restart = "Vuelve a Intentarlo! Solo puedes dar una 'patada' o una 'manada'"
    try:
      print(restart)
      player_2_atack()
    except NameError:
      pass

def player_2_defense():
    defense = input("Quieres cubrirte la cara o las patas?: ")
    defense = defense.upper()
    if defense == "CARA":
        print("El jugador 2 se cubrió la cara")
        defense_2 = "def_alta"
    elif defense == "PATAS":
        print("El jugador 2 se cubrió las patas")
        defense_2 = "def_baja"
    else:
        os.system("cls")
        restart = "Vuelve a Intentarlo! Solo puedes cubrirte la 'cara' o las 'patas'"
    try:
      print(restart)
      player_2_defense()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

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
os.system("cls")        #Límpia la pantalla
print ("Bienvenido!")   #Mensaje de Bienvenida
players()               #Sección 1 --- Cantidad de jugadores
#exports()               #Sección Final --- Exportar datos a Json
