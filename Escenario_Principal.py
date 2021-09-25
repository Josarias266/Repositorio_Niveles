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
pared.matar()
print(pared.estado())
pokemon = obstaculo("Metapod", 7, 9, True)
#pokemon.matar()
print(pokemon.estado())
dragon = obstaculo("Tohru", 20, 10, True)
dragon.matar()
print(dragon.estado())
koopa = obstaculo("Koopa-Troopa", 15, 11, True)
koopa.matar()
print(koopa.estado())

#Objetos FQ
momia1 = obstaculo("momia", 50, 20, True)
momia1.matar()
print(momia1.estado())
zombie1 = obstaculo("zombie", 40, 15, True)
#zombie1.matar()
print(zombie1.estado())

#Objetos JP
cuervo1 = obstaculo("Cuervo", 10000, 0, True)
#cuervo1.matar()
print(cuervo1.estado())
araña1 = obstaculo("Spider" , 10000, 0, True)
araña1.matar()
print(araña1.estado())

#Objetos RS
coco1 = obstaculo("Farm", 35, 50, True)
coco1.matar()
print(coco1.estado())
buitre1 = obstaculo("Jalks" , 25, 15, True)
#buitre1.matar()
print(buitre1.estado())

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
export.write(buitre1.estado())
export.close()

#Pendiente evaluar si el nivel es superado al vencer obstaculos
#Pendiente funcion para disminuir la resistencia
#Pendiente funcion de nueva habilidad jugador
#Pendiente nueva habilidad obstaculo
