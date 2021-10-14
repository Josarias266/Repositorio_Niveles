import os

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
            return "El jugador 1 escogió a " + (self.name)
        else:
            pass
    
    def escogido_2(self):
        if (self.selected_2):
            return "El jugador 2 escogió a " + (self.name)
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
reina = luchador("La Reina Izabel", 10, 1, False, False, False, False, False, False, True)
jackie = luchador("Jackie Chan", 10, 1, False, False, False, False, False, False, True)
#Avatares KA
trump = luchador("Trump", 10, 1, False, False, False, False, False, False, True)
messi = luchador("Messi Chikito", 10, 1, False, False, False, False, False, False, True)

def players():      #Sección 1 --- Cantidad de jugadores
    try:
        amount = int(input("Cuantos jugadores habrán? "))
        if amount == 1:
            player1_choose()
            bot_choose()
        elif amount == 2:
            player1_choose()
            player2_choose()
        else:
            input ("Solo pueden haber 1 o 2 jugadores, presiona enter para volver a intentarlo...")
            os.system ("cls")
            players()
    except ValueError:
        input ("Solo puedes introducir valores numéricos, presiona enter para volver a intertarlo...")
        os.system ("cls")
        players()

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
      input ("Presiona la tecla enter para empezar el juego...")
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
      input ("Presiona la tecla enter para empezar el juego...")
      os.system ("cls")

def player1_choose():
    print("Jugador 1 prepárate para escoger a tu luchador!")
    selection_1()

def player2_choose():
    print("Jugador 2 prepárate para escoger a tu luchador!")
    selection_2()

def bot_choose():
    player2_choose()

def prints_1():       #Sección Pre-Final --- Estado de los avatares 1
    if chabelo.selected_1:
        print(chabelo.escogido_1())
    elif tecun.selected_1:
        print(tecun.escogido_1())
    elif arjona.selected_1:
        print(arjona.escogido_1())
    elif gaby.selected_1:
        print(gaby.escogido_1())
    elif mcgregor.selected_1:
        print(mcgregor.escogido_1())
    elif jake.selected_1:
        print(jake.escogido_1())
    elif reina.selected_1:
        print(reina.escogido_1())
    elif siuu.selected_1:
        print(siuu.escogido_1())
    elif jackie.selected_1:
        print(jackie.escogido_1())
    elif trump.selected_1:
        print(trump.escogido_1())
    elif messi.selected_1:
        print(messi.escogido_2())
    else:
        pass

def prints_2():       #Sección Pre-Final --- Estado de los avatares 2
    if chabelo.selected_2:
        print(chabelo.escogido_2())
    elif tecun.selected_2:
        print(tecun.escogido_2())
    elif arjona.selected_2:
        print(arjona.escogido_2())
    elif gaby.selected_2:
        print(gaby.escogido_2())
    elif mcgregor.selected_2:
        print(mcgregor.escogido_2())
    elif jake.selected_2:
        print(jake.escogido_2())
    elif reina.selected_2:
        print(reina.escogido_2())
    elif siuu.selected_2:
        print(siuu.escogido_2())
    elif jackie.selected_2:
        print(jackie.escogido_2())
    elif trump.selected_2:
        print(trump.escogido_2())
    elif messi.selected_2:
        print(messi.escogido_2())
    else:
        pass

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
prints_1()              #Sección Pre-Final --- Estado de los avatares
prints_2()              #Sección Pre-Final --- Estado de los avatares
#exports()               #Sección Final --- Exportar datos a Json


input ("Presiona la tecla enter para salir...")