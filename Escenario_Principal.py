import os

class obstaculo:  #aquí se define la clase principal para los obstáculos
    def __init__(self, name, hp, ap, alive):  #aquí se define el constructor
        self.name = name
        self.hp = hp
        self.ap = ap
        self.alive = alive  #el estado por defecto del enemigo es "vivo", "True"

    def matar(self):  #método para cambiar el estado del enemigo a "muerto", "False"
        self.alive = False

    def estado(self):  #método para informar sobre el estado del enemigo
        if (self.alive):
            return "El enemigo " + (self.name) + " sigue con vida"

        else:
            return "El enemigo " + (self.name) + " ha muerto"

#Objetos JA
pared = obstaculo("Whomp", 10, 5, True)
pokemon = obstaculo("Metapod", 7, 9, True)
dragon = obstaculo("Tohru", 20, 10, True)
koopa = obstaculo("Koopa-Troopa", 15, 11, True)

#Objetos FQ
momia1 = obstaculo("momia", 50, 20, True)
zombie1 = obstaculo("zombie", 40, 15, True)

#Objetos JP
cuervo1 = obstaculo("Cuervo", 10000, 0, True)
araña1 = obstaculo("Spider" , 10000, 0, True)

#Objetos RS
coco1 = obstaculo("Farm", 35, 50, True)
buitre1 = obstaculo("Jalks" , 25, 15, True)

#Objetos KA
wolfman = obstaculo("Lucas", 7, 7, True)
vampire = obstaculo("Dracula", 8, 6, True)

print ("Bienvenido!")
def select():
    print ("Escoje un Enemigo de la lista para derrotarlo!")
    print ("Whomp")
    print ("Metapod")
    print ("Tohru")
    print ("Koopa Troopa")
    print ("Momia")
    print ("Zombi")
    print ("Spider")
    print ("Cuervo")
    print ("Farm")
    print ("Jalks")
    print ("Lucas")
    print ("Drácula")

    def defeat():
        defeated.matar()

    choice = input("¿Qué enemigo quieres derrotar?: ")
    choice = choice.upper()
    if choice == "WHOMP":
        defeated = pared
        defeat()
    elif choice == "METAPOD":
        defeated = pokemon
        defeat()
    elif choice == "TOHRU":
        defeated = dragon
        defeat()
    elif choice == "KOOPA TROOPA":
        defeated = koopa
        defeat()
    elif choice == "MOMIA":
        defeated = momia1
        defeat()
    elif choice == "ZOMBI":
        defeated = zombie1
        defeat()
    elif choice == "SPIDER":
        defeated = araña1
        defeat()
    elif choice == "CUERVO":
        defeated = cuervo1
        defeat()
    elif choice == "FARM":
        defeated = coco1
        defeat()
    elif choice == "JALKS":
        defeated = buitre1
        defeat()
    elif choice == "LUCAS":
        defeated = wolfman
        defeat()
    elif choice == "DRACULA":
        defeated = vampire
        defeat()
    else:
        os.system ("cls") # "cls" en windows y "clear" en mac/replit
        restart = "Intentalo de Nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      select()
    except NameError:
      input ("Presiona la tecla enter para ver los resultados...")
      os.system ("cls")
      
select()

#Estado final de los enemigos
print(pared.estado())
print(pokemon.estado())
print(dragon.estado())
print(koopa.estado())
print(momia1.estado())
print(zombie1.estado())
print(cuervo1.estado())
print(araña1.estado())
print(coco1.estado())
print(buitre1.estado())
print(wolfman.estado())
print(vampire.estado())

input ("Presiona la tecla enter para salir...")


#Exportar datos a Json
export = open("Resultados_Nivel.json", "w")
export.write("Estos son los resultados del nivel: \n")
export.write(pared.estado() + "\n")
export.write(pokemon.estado() + "\n")
export.write(dragon.estado() + "\n")
export.write(koopa.estado() + "\n")
export.write(momia1.estado() + "\n")
export.write(zombie1.estado() + "\n")
export.write(araña1.estado() + "\n")
export.write(cuervo1.estado() + "\n")
export.write(coco1.estado() + "\n")
export.write(buitre1.estado() + "\n")
export.write(wolfman.estado() + "\n")
export.write(vampire.estado())
export.close()

#Pendiente evaluar si el nivel es superado al vencer obstaculos
#Pendiente funcion para disminuir la resistencia
#Pendiente funcion de nueva habilidad jugador
#Pendiente nueva habilidad obstaculo