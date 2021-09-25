import os
print ("Bienvenido!")
def select():
    print ("Escoje un Enemigo de la lista para derrotarlo!")
    print ("Whomp")
    print ("Metapod")
    print ("Tohru")
    print ("Koopa-Troopa")
    print ("Momia")
    print ("Zombi")
    print ("Spider")
    print ("Cuervo")
    print ("Farm")
    print ("Jalks")
    print ("Lucas")
    print ("Drácula")

    def defeat():
        print ("Felicidades! Has derrotado a " + (defeated))

    choice = input("¿Qué enemigo quieres derrotar?: ")
    choice = choice.upper()
    if choice == "WHOMP":
        defeated = "Whomp"
        defeat()
    elif choice == "METAPOD":
        defeated = "Metapod"
        defeat()
    elif choice == "TOHRU":
        defeated = "Tohru"
        defeat()
    elif choice == "KOOPA TROOPA":
        defeated = "Koopa-Troopa"
        defeat()
    elif choice == "MOMIA":
        defeated = "Momia"
        defeat()
    elif choice == "ZOMBI":
        defeated = "Zombi"
        defeat()
    elif choice == "SPIDER":
        defeated = "Spider"
        defeat()
    elif choice == "CUERVO":
        defeated = "Cuervo"
        defeat()
    elif choice == "FARM":
        defeated = "Farm"
        defeat()
    elif choice == "JALKS":
        defeated = "Jalks"
        defeat()
    elif choice == "LUCAS":
        defeated = "Lucas"
        defeat()
    elif choice == "DRACULA":
        defeated = "Dracula"
        defeat()
    else:
        os.system ("cls") # "cls" en windows y "clear" en mac/replit
        restart = "Intentalo de Nuevo y asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien"
    
    try:
      print(restart)
      select()
    except NameError:
      input ("Eso fue todo, presiona la tecla enter para salir...")
      
select()