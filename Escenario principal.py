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


momia1 = villanos("momia", 20, 3, True) 
zombie1 = villanos("zombie", 20, 5, False)
jugador = villanos("jugador", 20, 3, True)


momia1.atacar(jugador)
jugador.atacar(momia1)