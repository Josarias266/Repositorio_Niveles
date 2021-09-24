class obstaculo:  #aquí se define la clase principal para los obstáculos
    def __init__(self, name, hp, ap, alive):  #aquí se define el constructor
        self.name = name
        self.hp = hp
        self.ap = ap
        self.alive = alive  #el estado por defecto del enemigo es "vivo"

    def matar(self):  #método para cambiar el estado del enemigo a "muerto"
        self.alive = False

    def estado(self):  #método para informar sobre el estado del enemigo
        if (self.alive):
            return "El enemigo " + (self.name) + " sigue con vida"

        else:
            return "El enemigo " + (self.name) + " ha muerto"


pared = obstaculo("Mural", 10, 5, True)
pared.matar()
print(pared.estado())
perro = obstaculo("Firulais", 7, 9, True)
#perro.matar()
print(perro.estado())
dragon = obstaculo("Tohru", 20, 10, True)
dragon.matar()
print(dragon.estado())
koopa = obstaculo("koopa-tropa", 20, 10, True)
koopa.matar()
print(koopa.estado())

#Exportar datos a Json
export = open("Prueba.json", "w")
export.write("Estos son los resultados del nivel: \n")
export.write(pared.estado() + "\n")
export.write(perro.estado() + "\n")
export.write(dragon.estado() + "\n")
export.write(koopa.estado())
export.close()

#Pendiente evaluar si el nivel es superado al vencer obstaculos
#Pendiente funcion para disminuir la resistencia
#Pendiente funcion de nueva habilidad jugador
#Pendiente nueva habilidad obstaculo
