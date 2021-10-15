#--------------------------------------------------Importaciones :v---------------------------------------------------
import os           #Aquí se importan los comandos del sistema
import random       #Aquí se importa la librería para "funciones de azar"

#--------------------------------------------------Clase "Luchador"----------------------------------------------------
class luchador:     #Aquí se define la clase principal para los avatares
    def __init__(self, name, hp, ap, selected_1, selected_2, alive):  #aquí se define el constructor
        self.name = name                    #nombre del luchador
        self.hp = hp                        #puntos de salud del luchador
        self.ap = ap                        #puntos de ataque del luchador
        self.selected_1 = selected_1        #seleccionado por el jugador 1, por defecto "False"
        self.selected_2 = selected_2        #seleccionado por el jugador 2, por defecto "False"
        self.alive = alive                  #el estado por defecto del luchador es "vivo", "True"

    def matar(self):  #método para cambiar el estado del enemigo a "muerto", "False"
        self.alive = False

    def character_1(self):  #método para indicar si el luchador es seleccionado por el jugador 1
        self.selected_1 = True
        global peleador_1
        peleador_1 = self.name
        global hp_1
        hp_1 = self.hp
        global ap_1
        ap_1 = self.ap

    def character_2(self):  #método para indicar si el luchador es seleccionado por el jugador 2
        self.selected_2 = True
        global peleador_2
        peleador_2 = self.name
        global hp_2
        hp_2 = self.hp
        global ap_2
        ap_2 = self.ap

#-----------------------------------------Listado de Luchadores Disponibles---------------------------------------------
#Avatares JA
chabelo = luchador("Chabelo", 3, 1, False, False, True)
tecun = luchador("Tecún Uman", 3, 1, False, False, True)
#Avatares FQ
arjona = luchador("Ricardo Arjona", 3, 1, False, False, True)
gaby = luchador("Gaby Moreno", 3, 1, False, False, True)
mcgregor = luchador("Conor Mcgregor", 3, 1, False, False, True)
#Avatares JP
jake = luchador("Jake Paul", 3, 1, False, False, True)
siuu = luchador("El Bicho", 3, 1, False, False, True)
#Avatares RS
reina = luchador("La Reina Isabel", 3, 1, False, False, True)
jackie = luchador("Jackie Chan", 3, 1, False, False, True)
#Avatares KA
trump = luchador("Trump", 3, 1, False, False, True)
messi = luchador("Messi Chikito", 3, 1, False, False, True)

#--------------------------------------------------Funciones------------------------------------------------------------
def preparativos():                 #Precedentes del código principal
    os.system("title -_-_-_-_-_-_-_-_-_-_-_-_-_-World All Stars Brawl-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    os.system("color 30")
    os.system("font_music_mk.mp3")
    os.system("alt_tab.bat")

def clean_screen():                 #Función para limpiar pantalla
    try:
        os.system("cls")    #En caso de usar Windows
    except:
        os.system("clear")  #En caso de usar Replit/iOS/Linux

def bienvenida():                   #Sección 0 --- Pantalla de Bienvenida al Usuario
    os.system("animacion.bat")
    clean_screen()
    print ("Bienvenido!")

def players():                      #Sección 1 --- Cantidad de Jugadores Humanos
    try:
        amount = int(input("Cuantos jugadores habrán? "))
        if amount == 1:
            os.system ("cls")
            global human_players
            human_players = 1
            player1_choose()        #Sección 1.1 v1
            bot_choose()            #Sección 1.1 v3
        elif amount == 2:
            os.system ("cls")
            human_players = 2
            player1_choose()        #Sección 1.1 v1
            player2_choose()        #Sección 1.1 v2
        else:
            input ("Solo pueden haber 1 o 2 jugadores, presiona enter para volver a intentarlo...")
            os.system ("cls")
            players()
    except ValueError:
        input ("Solo puedes introducir valores numéricos, presiona enter para volver a intentarlo...")
        os.system ("cls")
        players()

def player1_choose():               #Sección 1.1 v1 --- Función para que el jugador 1 escoja luchador
    print("Jugador 1 prepárate para escoger a tu luchador!")
    selection_1()

def player2_choose():               #Sección 1.1 v2 --- Función para que el jugador 2 escoja luchador
    print("Jugador 2 prepárate para escoger a tu luchador!")
    selection_2()

def bot_choose():                   #Sección 1.1 v3 --- Función para que el bot escoja luchador

    def choice():
        fighter_2.character_2()

    choose = random.randint(1,11)
    if choose == 1:
        global fighter_2
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

def selection_1():                  #Sección 1.1.1 v1 --- Jugador 1 Escoge un Luchador de la lista
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
        global fighter_1
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
        restart = "Jugador 1 intentalo de nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      selection_1()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

def selection_2():                  #Sección 1.1.1 v2 --- Jugador 2 Escoge un Luchador de la lista
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
        global fighter_2
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
        restart = "Jugador 2 intentalo de nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      selection_2()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

def index_2():                      #Sección 2 --- Índice secundario | Desarrollo del juego
    print("El jugador 1 escogió a", fighter_1.name)
    print("El jugador 2 escogió a", fighter_2.name)
    input ("Presiona la tecla enter para iniciar el juego...")
    os.system("font_music.mp3")
    os.system("alt_tab.bat")
    clean_screen()
    while (fighter_1.alive) and (fighter_2.alive):
        print ("Turno del Jugador 1 |", fighter_1.name + "!")
        player_1_atack()
        player_1_defense()
        if human_players == 1:
            bot_atack()
            bot_defense()
            input ("Presiona la tecla enter para ver los resultados...")
            os.system ("cls")
            resultados_jugada()
            os.system ("cls")
        elif human_players == 2:
            print ("Turno del Jugador 2 |", fighter_2.name + "!")
            player_2_atack()
            player_2_defense()
            resultados_jugada()

def player_1_atack():               #Sección 2.1 v1 --- Ataque del jugador 1

    punch = input("Quieres tirar una patada o una manada?: ")
    punch = punch.upper()
    if punch == "PATADA":
        print("---" + peleador_1, "se prepara para patear---")
        global punch_1
        punch_1 = "patada"
        
    elif punch == "MANADA":
        print("---" + peleador_1, "reune todo su ki en su puño---")
        punch_1 = "manada"
        
    else:
        clean_screen()
        restart = "Jugador 1 Vuelve a Intentarlo! Solo puedes dar una 'patada' o una 'manada'"
    try:
      print(restart)
      player_1_atack()
    except NameError:
      pass

def player_1_defense():             #Sección 2.2 v1 --- Defensa del jugador 1
    defense = input("Quieres cubrirte la cara o las patas?: ")
    defense = defense.upper()
    if defense == "CARA":
        print("---" + peleador_1, "se coloca un casco---")
        global defense_1
        defense_1 = "def_alta"
    elif defense == "PATAS":
        print("---" + peleador_1, "se coloca espinilleras---")
        defense_1 = "def_baja"
    else:
        clean_screen()
        restart = "Jugador 1 Vuelve a Intentarlo! Solo puedes cubrirte la 'cara' o las 'patas'"
    try:
      print(restart)
      player_1_defense()
    except NameError:
      input ("Presiona la tecla enter para continuar...")
      os.system ("cls")

def player_2_atack():               #Sección 2.1 v2 --- Ataque del jugador 2
    punch = input("Quieres tirar una patada o una manada?: ")
    punch = punch.upper()
    if punch == "PATADA":
        print("---" + peleador_2, "se prepara para patear---")
        global punch_2
        punch_2 = "patada"
    elif punch == "MANADA":
        print("---" + peleador_2, "reune todo su ki en su puño---")
        punch_2 = "manada"
    else:
        clean_screen()
        restart = "Jugador 2 Vuelve a Intentarlo! Solo puedes dar una 'patada' o una 'manada'"
    try:
      print(restart)
      player_2_atack()
    except NameError:
      pass

def player_2_defense():             #Sección 2.2 v2 --- Defensa del jugador 2
    defense = input("Quieres cubrirte la cara o las patas?: ")
    defense = defense.upper()
    if defense == "CARA":
        print("---" + peleador_2, "se coloca un casco---")
        global defense_2
        defense_2 = "def_alta"
    elif defense == "PATAS":
        print("---" + peleador_2, "se coloca espinilleras---")
        defense_2 = "def_baja"
    else:
        clean_screen()
        restart = "Jugador 2 Vuelve a Intentarlo! Solo puedes cubrirte la 'cara' o las 'patas'"
    try:
      print(restart)
      player_2_defense()
    except NameError:
      input ("Presiona la tecla enter para ver los resultados...")
      os.system ("cls")

def bot_atack():                    #Sección 2.1 v3 --- Ataque del bot
	punch = random.randint(1,2)
	if punch == 1:
	    print("---" + peleador_2, "se prepara para patear---")
	    global punch_2
	    punch_2 = "patada"
	elif punch == 2:
	    print("---" + peleador_2, "reune todo su ki en su puño---")
	    punch_2 = "manada"

def bot_defense():                  #Sección 2.2 v3 --- Defensa del bot
	defense = random.randint(1,2)
	if defense == 1:
	    print("---" + peleador_2, "se coloca un casco---")
	    global defense_2
	    defense_2 = "def_alta"
	elif defense == 2:
	    print("---" + peleador_2, "se coloca espinilleras---")
	    defense_2 = "def_baja"

def resultados_jugada():            #Sección 2.3 --- Resultados de la jugada actual
    if punch_1 == "patada" and defense_2 == "def_alta":
        print (fighter_1.name, "le dió una patada de power ranger a", fighter_2.name, "y tremendo daño el que le hace!!!")
        player_1_point()
    elif punch_1 == "patada" and defense_2 == "def_baja":
        print (fighter_1.name, "falló la patada de power ranger y", fighter_2.name, "ni se inmuta!!!")
    elif punch_1 == "manada" and defense_2 == "def_alta":
        print (fighter_1.name, "falló el falcon punch y", fighter_2.name, "ni se inmuta!!!")
    elif punch_1 == "manada" and defense_2 == "def_baja":
        print (fighter_1.name, "le dió un falcon punch a", fighter_2.name, "y tremendo daño el que le hace!!!")
        player_1_point()

    if punch_2 == "patada" and defense_1 == "def_alta":
        print (fighter_2.name, "le dió una patada de power ranger a", fighter_1.name, "y tremendo daño el que le hace!!!")
        player_2_point()
    elif punch_2 == "patada" and defense_1 == "def_baja":
        print (fighter_2.name, "falló la patada de power ranger y", fighter_1.name, "ni se inmuta!!!")
    elif punch_2 == "manada" and defense_1 == "def_alta":
        print (fighter_2.name, "falló el falcon punch y", fighter_1.name, "ni se inmuta!!!")
    elif punch_2 == "manada" and defense_1 == "def_baja":
        print (fighter_2.name, "le dió un falcon punch a", fighter_1.name, "y tremendo daño el que le hace!!!")
        player_2_point()
    print("Vida restante de", fighter_1.name + ":" , hp_1)
    print("Vida restante de", fighter_2.name + ":" , hp_2)
    input("Presiona enter para volver a intentarlo...")
    os.system ("cls")

def player_1_point():               #Sección 2.3.1 v1 --- Función por si el jugador 1 da un golpe
    global hp_2
    hp_2 = hp_2-ap_1
    if hp_2 <= 0:
        fighter_2.matar()
        global winner
        winner = fighter_1.name
        global loser
        loser = fighter_2.name

def player_2_point():               #Sección 2.3.1 v2 --- Función por si el jugador 2 da un golpe
    global hp_1
    hp_1 = hp_1-ap_2
    if hp_1 <= 0:
        fighter_1.matar()
        global winner
        winner = fighter_2.name
        global loser
        loser = fighter_1.name

def resultados_finales():           #Sección 3 --- Presentación de Resultados
    print(loser, "ha muerto")
    print("El ganador es:", winner)
    input("Presiona enter para salir...")
    os.system("taskkill /f /im music.ui.exe")

def exports():                      #Sección Final --- Exportar datos a Json --- (Pendiente)
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

#-----------------------------------Índice principal de Secciones del código--------------------------------------------
input("Presiona 'enter' para empezar con la magia XD...")
preparativos()                      #Precedentes del código principal
bienvenida()                        #Sección 0 --- Pantalla de Bienvenida al Usuario
players()                           #Sección 1 --- Cantidad de Jugadores Humanos
index_2()                           #Sección 2 --- Índice secundario | Desarrollo del juego
resultados_finales()                #Sección 3 --- Presentación de Resultados