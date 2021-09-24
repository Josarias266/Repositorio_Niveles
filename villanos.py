class villanos:
    def __init__(self,nombre,hp,ap,escudo,sp,time):
        self.nombre = nombre
        self.hp = hp
        self.ap = ap
        self.escudo = escudo
        self.sp = sp
        self.time = time

    def __str__(self):
        return self.nombre

    def atacar (self, jugador):
        if jugador.escudo:
            self.salud -= self.ataque
        else:
            jugador.salud -= self.ataque
        print("{} ataca a {}".format(self.nombre, jugador))
        print("{} tiene de salud {}".format(self, self.salud))
        print("{} tiene de salud {}".format(jugador, jugador.salud))


cuervo1 = villanos("Cuervo", 10000, 0, 0, 16, 8)
araña1 = villanos("Araña" , 10000, 0, 10, 5, 15)